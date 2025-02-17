from django.urls import path
from .views import GalleryListView, ProjectDetailView, ProjectListView, SkillListView, TechnologyListView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('technologies/',
         TechnologyListView.as_view(), name='technology-list'),
    path('projects/<int:project_id>/',
         ProjectDetailView.as_view(), name='project-details'),
]
