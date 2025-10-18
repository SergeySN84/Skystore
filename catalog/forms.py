from django import forms
from .models import Product

FORBIDDEN_WORDS = {
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    def _check_forbidden_words(self, value):
        """Проверяет наличие запрещённых слов (регистронезависимо)"""
        if not value:
            return
        words = set(word.lower() for word in value.split())
        if FORBIDDEN_WORDS & words:
            raise forms.ValidationError(
                "Текст содержит запрещённые слова: казино, криптовалюта, крипта, биржа, "
                "дешево, бесплатно, обман, полиция, радар."
            )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self._check_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self._check_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price
