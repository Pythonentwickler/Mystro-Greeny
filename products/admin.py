from django.contrib import admin

# Register your models here.
from .models import Product,ProductImage,ProductReview,Category,Brand

class ProductImagAdmin(admin.TabularInline,):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'flag', 'price']
    inlines = [ProductImagAdmin]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Brand)