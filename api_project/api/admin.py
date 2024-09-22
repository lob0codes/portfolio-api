from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProductAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('title', 'description', 'url', 'image')
