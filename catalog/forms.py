from django import forms

from catalog.models import Product, Category, Version


# Форма для продукта
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        # Список запрещенных к использованию слов
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        # Проверяем наличие запрещенных слов в названии или описании продукта
        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError('Нельзя добавлять запрещенные слова в название или описание продукта.')


# Форма для Категорий
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# Форма для версии продукта
class ProductVersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['number', 'name', 'is_active']
        