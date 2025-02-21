from django import forms
from dishes.models import Dish

class DishModelForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ['name', 'description', 'category', 'price', 'photo']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'category': 'Categoria',
            'price': 'Preço', 
            'photo': 'Foto',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'category': forms.Select(attrs={'class': 'input'}),
            'description': forms.TextInput(attrs={'class': 'input'}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
        }