from django.contrib import admin
from .models import Challenge, Gallery, NextStep, Project, ProjectDetail, Tag, Skill, Technology


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1  # Number of extra empty forms to display


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('title', 'description', 'url', 'image')
    inlines = [GalleryInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('name', 'icon')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('name', 'image', 'experience')


class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 1  # Number of extra empty forms to display


class NextStepInline(admin.TabularInline):
    model = NextStep
    extra = 1  # Number of extra empty forms to display


@admin.register(ProjectDetail)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_title', 'description')
    inlines = [ChallengeInline, NextStepInline]

    def project_id(self, obj):
        return obj.project.id
    project_id.short_description = 'Project ID'

    def project_title(self, obj):
        return obj.project.title
    project_title.short_description = 'Project Title'


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('id', 'name', 'image', 'description')
