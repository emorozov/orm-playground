import random

import factory.fuzzy
from django.contrib.contenttypes.models import ContentType

from . import models


class StatusFactory(factory.django.DjangoModelFactory):
    text = factory.Iterator(['создан', 'активен', 'неактивен', 'выпущен'])

    class Meta:
        model = models.Status


class CohortFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('job')

    class Meta:
        model = models.Cohort


class StudentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    status = factory.fuzzy.FuzzyChoice(models.Status.objects.all())

    class Meta:
        model = models.Student


class StudentCohortFactory(factory.django.DjangoModelFactory):
    cohort = factory.fuzzy.FuzzyChoice(models.Cohort.objects.all())
    student = factory.fuzzy.FuzzyChoice(models.Student.objects.all())

    class Meta:
        model = models.StudentCohort


class StudentActivityLogFactory(factory.django.DjangoModelFactory):
    activity = factory.fuzzy.FuzzyChoice(models.ActivityLog.Action.choices,
                                         getter=lambda c: c[0])
    content_type = factory.LazyAttribute(lambda o: ContentType.objects.get_for_model(models.Student))
    object_id = factory.fuzzy.FuzzyChoice(models.Student.objects.values_list('pk', flat=True))

    class Meta:
        model = models.ActivityLog


class CohortActivityLogFactory(StudentActivityLogFactory):
    content_type = factory.LazyAttribute(lambda o: ContentType.objects.get_for_model(models.Cohort))
    object_id = factory.fuzzy.FuzzyChoice(models.Cohort.objects.values_list('pk', flat=True))
