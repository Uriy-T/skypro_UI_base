from pathlib import Path
import json
from typing import Any

from django.core.management.base import BaseCommand

from catalog.models import Category, Product
from configuration import CATALOG_FIXTURES


def fixture_reader(path_to_fixture: Path) -> dict[str: Any]:
    with open(path_to_fixture, 'r', encoding='utf-8') as fixture:
        records = json.load(fixture)
    return records


class Command(BaseCommand):
    help = 'Clear table catalog_products and add basic list of products'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        products_data = [record['fields'] for record in fixture_reader(CATALOG_FIXTURES)
                         if record['model'] == 'catalog.product']


        for product in products_data:
            try:
                category = Category.objects.get(pk=product['product_category'])

            except Category.DoesNotExist:
                self.stderr.write(self.style.WARNING('Категория не существует. Продукт пропущен.'))
                continue

            new_product = Product.objects.create(product_name=product['product_name'],
                                   description=product['description'],
                                   product_category=category,
                                   price_per_unit=product['price_per_unit'])

            self.stdout.write(self.style.SUCCESS(f'Продукт {new_product.product_name} создан.'))

