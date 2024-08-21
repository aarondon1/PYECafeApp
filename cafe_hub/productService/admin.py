from django.contrib import admin

from productService.models import ProductService
from main.models import Branch

# Register your models here.

class ProductSeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'video', 'link', 'branch']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        if request.user.branch:
            return qs.filter(id=request.user.branch.id)
        else:
            return qs.none()


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['branch'].queryset = Branch.objects.filter(id=request.user.branch.id)
        return form
    
admin.site.register(ProductService, ProductSeviceAdmin)