from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]#what i want to show here
    prepopulated_fields = {'slug': ('name',)}#specifies the filed name of the category such as media

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price','in_stock', 'lowCarb', 'keto', 'vegan', 'created', 'updated']
    list_filter = ['lowCarb', 'keto', 'vegan', 'is_active', 'in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug':('title',)}


