import django.db
from django.core.management.base import BaseCommand

from orm.students.factories import (
    StatusFactory, CohortFactory, StudentFactory, StudentCohortFactory, StudentActivityLogFactory,
    CohortActivityLogFactory
)


class Command(BaseCommand):
    help = 'Заполняет базу данных сгенерированными данными.'

    def handle(self, *args, **options):
        for _ in range(4):
            StatusFactory()

        for _ in range(20):
            try:
                CohortFactory()
            except django.db.utils.IntegrityError:
                # Игнорируем повторяющиеся названия когорт
                pass

        for _ in range(200):
            try:
                StudentFactory()
            except django.db.utils.IntegrityError:
                # Игнорируем повторяющиеся имена студентов
                pass

        for _ in range(300):
            try:
                StudentCohortFactory()
            except django.db.utils.IntegrityError:
                # Игнорируем повторяющиеся пары студент-когорта
                pass

        for _ in range(200):
            StudentActivityLogFactory()
            CohortActivityLogFactory()
