from django.contrib import admin
from product.models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible', 'weight')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'category', 'created_time')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)