from django.contrib import admin
from dishes.models import Category, Dish

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Dish)
class DishModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'description', 'name', 'price')
    search_fields = ('category', 'name')