from django.contrib import admin
from .models import Project, Tag


@admin.register(Project)
class ProductAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('title', 'description', 'url', 'image')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('name', 'icon')
