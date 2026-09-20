import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.constants import (INGREDIENTS_CSV_FILENAME,
                               INGREDIENTS_CSV_PATH)
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает ингредиенты из CSV-файла'

    def handle(self, *args, **options):
        possible_paths = [
            Path(INGREDIENTS_CSV_PATH),
            Path(settings.BASE_DIR).parent / 'data' / INGREDIENTS_CSV_FILENAME,
            Path(settings.BASE_DIR) / 'data' / INGREDIENTS_CSV_FILENAME,
        ]

        file_path = None
        for p in possible_paths:
            if p.exists():
                file_path = p
                break

        if not file_path:
            self.stdout.write(self.style.ERROR(
                f'Файл не найден. Искали в: {possible_paths}'
            ))
            return

        self.stdout.write(f'Загружаем из: {file_path}')

        with open(file_path, encoding='utf-8') as f:
            reader = csv.reader(f)
            created = 0
            for row in reader:
                if len(row) == 2:
                    _, was_created = Ingredient.objects.get_or_create(
                        name=row[0].strip(),
                        measurement_unit=row[1].strip()
                    )
                    if was_created:
                        created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Загружено ингредиентов: {created}')
        )
