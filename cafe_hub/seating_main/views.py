from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Seat
from .decorators import allowed_users

def homepage(request):
    items = Seat.objects.all()
    try:
        booked_seats = Seat.objects.filter(user=request.user)
    except:
        booked_seats = None
    
    is_staff = request.user.groups.filter(name='staff').exists()
    
    return render(request, "seating_main/home.html", {"seats": items, "booked_seats": booked_seats, "is_staff": is_staff})


def update_seat_availability(request, seat_id):
    if request.user.is_authenticated:    
        if request.method == "POST":
            seat = Seat.objects.get(id=seat_id)
            if seat.available:
                seat.available = False
                seat.user = request.user
            else:
                seat.available = True
                seat.user = None
            seat.save()
            return redirect("/")
        else:
            messages(request, "You need to be logged in to book a seat")
            return redirect("/")
    return render(request, "seating_main/home.html", {"seats": Seat.objects.all()})

@allowed_users(allowed_roles=["staff", "admin"])  
def staffpage(request):
    items = Seat.objects.all()
    return render(request, "seating_main/staff.html", {"seats": items})
@allowed_users(allowed_roles=["staff", "admin"])
def staff_update_seat_availability(request, seat_id):
    if request.method == "POST":
        seat = Seat.objects.get(id=seat_id)
        if seat.available:
            seat.available = False
            seat.user = None
        else:
            seat.available = True
            seat.user = None
        seat.save()
        return redirect("/staff/")
    return render(request, "seating_main/staff.html", {"seats": Seat.objects.all()})
@allowed_users(allowed_roles=["staff", "admin"])
def staff_add_seat(request):
    if request.method == "POST":
        seat_name = request.POST.get("seat_name")
        new_seat = Seat(name=seat_name, available=True)
        new_seat.save()
        return redirect("/staff/")
    return render(request, "seating_main/staff.html", {"seats": Seat.objects.all()})

@allowed_users(allowed_roles=["staff", "admin"])
def staff_delete_seat(request, seat_id):
    if request.method == "POST":
        seat = Seat.objects.get(id=seat_id)
        seat.delete()
    
    
    return redirect("/staff/")