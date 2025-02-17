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

    def __str__(self):
        return self.title


class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'projects_details'


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    project_detail = models.ForeignKey(
        ProjectDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = 'challenges'


class NextStep(models.Model):
    title = models.CharField(max_length=255)
    project_detail = models.ForeignKey(
        ProjectDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = 'next_steps'


class Technology(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ManyToManyField(Project, blank=True)

    class Meta:
        db_table = 'technologies'
        verbose_name_plural = "Technologies"


class Gallery(models.Model):
    images = models.JSONField(default=list)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "galleries"
        verbose_name_plural = "Galleries"
