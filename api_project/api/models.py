from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class ExperiencieLevel(models.TextChoices):
        BEGINNER = 'Beginner', 'Beginner'
        INTERMEDIATE = 'Intermediate', 'Intermediate'
        PROFICIENT = 'Proficient', 'Proficient'

    experience = models.CharField(
        max_length=20,
        choices=ExperiencieLevel.choices,
        default=ExperiencieLevel.BEGINNER
    )

    class Meta:
        db_table = 'skills'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    class Meta:
        db_table = 'tags'


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'projects'
