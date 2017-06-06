from django import forms
from .models import Category

class CategoryModel(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию",
                                       widget=forms.Select(attrs={'category': 'dropdown'}), label="Категория")

    class Meta:
        model = Category
        fields = ('name',)