from django.contrib import admin
from dishes.models import Category

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', )