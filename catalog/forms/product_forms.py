import os

from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from configuration import RESTRICTED_WORDS, P_IMAGE_TYPES, P_SIZE_LIMIT

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'product_image', 'product_category', 'price_per_unit']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        for word in RESTRICTED_WORDS:
            if word in product_name:
                raise ValidationError(f'"{word}" не может быть в составе значения поля "Название продукта".')
        return product_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in RESTRICTED_WORDS:
            if word in description:
                raise ValidationError(f'"{word}" не может быть в составе значения поля "Название продукта".')
        return description

    def clean_product_image(self):
        image = self.cleaned_data.get('product_image')
        if not image:
            return image

        size_mb_limit = P_SIZE_LIMIT * 1024 * 1024
        if image.size > size_mb_limit:
            raise ValidationError(f'Размер загружаемого изображения превышает установленный лимит ({P_SIZE_LIMIT} мб)')

        available_formats = P_IMAGE_TYPES
        actual_type = os.path.splitext(image.name)[1].lower()
        if actual_type not in available_formats:
            raise ValidationError(f'Для загрузки допустимы изображения форматов: {", ".join(P_IMAGE_TYPES)}')

        return image


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта',
            'required': 'required'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['product_image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['product_category'].widget.attrs.update({
            'class': 'form-select',
            'required': 'required'
        })

        self.fields['price_per_unit'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену продукта',
            'required': 'required'
        })
