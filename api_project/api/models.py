from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image = models.CharField(max_length=255)

    class Meta:
        db_table = 'projects'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    class Meta:
        db_table = 'tags'
