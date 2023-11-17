from django import forms
from .models import Product

class OptionsVendinha(forms.Form):
    options = (
        ('BRUM', 'BRUM'),
        ('TIRADENTES', 'TIRADENTES'),
        ('APOLLO', 'APOLLO'),
    )
    Selecione = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect(attrs={'class': 'vertical-radio'})
    )


class ReviewForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Selecione o Produto para Avaliar"
    )
    rating = forms.IntegerField(
        label="Classificação (de 1 a 5)",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 5}),
    )
    comment = forms.CharField(
        label="Comentário",
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False 
    )
