from rest_framework import generics

from .models import Gallery, Project, ProjectDetail, Skill, Technology
from .serializers import GallerySerializer, ProjectSerializer, SkillSerializer, ProjectDetailSerializer, TechnologySerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    # Match this with the URL pattern and the model relationship
    lookup_field = 'project_id'

    def get_queryset(self):
        # Filter down to only relevant records to avoid fetching all
        return ProjectDetail.objects.filter(project_id=self.kwargs['project_id'])


class GalleryListView(generics.ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            return Gallery.objects.filter(project_id=project_id)
        return Gallery.objects.all()


class TechnologyListView(generics.ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            return Technology.objects.filter(project__id=project_id)
        return Technology.objects.all()
