from django.contrib import admin
from .models import Category, Product
# Модель категории
# prepopulated_fields - используется для поля slug, которе будет автоматически генерироваться на основе названия товара
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


# Модель товара
#list_editable - позволяет задать те поля, которые можно будет редактировать на странице со списком товаров,
# любой из в этом наборе должен присутствовать и в list_display
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
