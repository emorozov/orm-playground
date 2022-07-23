from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Status(models.Model):
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Statuses'


class StudentCohort(models.Model):
    cohort = models.ForeignKey('Cohort', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cohort', 'student')


class Cohort(models.Model):
    name = models.TextField('Название когорты', primary_key=True)
    students = models.ManyToManyField('Student', related_name='cohorts', through=StudentCohort)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.TextField(unique=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class ActivityLog(models.Model):
    class Action(models.IntegerChoices):
        CREATE = 1
        UPDATE = 2
        DELETE = 3

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.TextField()
    content_object = GenericForeignKey('content_type', 'object_id')
    activity = models.IntegerField(choices=Action.choices)

    def __str__(self):
        return f'{self.content_object} {self.activity}'

