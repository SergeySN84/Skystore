from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Загружает тестовые данные: сначала удаляет старые, затем загружает фикстуры."

    def handle(self, *args, **options):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Старые данные удалены."))

        # Загружаем фикстуры
        call_command('loaddata', 'categories', verbosity=0)
        call_command('loaddata', 'products', verbosity=0)

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены!"))
