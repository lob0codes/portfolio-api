from rest_framework import serializers

from .models import Project, Skill, Tag, ProjectDetail, \
    Challenge, NextStep, Technology, Gallery


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'image', 'experience']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'icon']


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'tags', 'url']


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title']


class NextStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextStep
        fields = ['id', 'title']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'image', 'description']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'images']


class ProjectDetailSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(
        source='project.title', read_only=True)
    challenges = ChallengeSerializer(many=True, source='challenge_set')
    next_steps = NextStepSerializer(many=True, source='nextstep_set')

    class Meta:
        model = ProjectDetail
        fields = ['id', 'project_id', 'project_name', 'description', 'challenges',
                  'next_steps']
