from django.contrib import admin
from .models import Category,Product

# Register your models here.
@admin.register(Category)
class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name', )}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'slug','price','avilable','created','updated']
    list_filter =['avilable','created','updated']
    list_editable = ['price','avilable']
    prepopulated_fields = {'slug':('name' ,)}