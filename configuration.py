from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()

CATALOG_FIXTURES = PROJECT_ROOT/'catalog_fixture.json'

STANDART_LOGO = PROJECT_ROOT/'main/img/box_group.png'


RESTRICTED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

# Типы допустимых форматов изображений для создания продуктов (префикс - P).
P_IMAGE_TYPES = ['.jpeg', '.png', '.jpg']
P_SIZE_LIMIT = 5