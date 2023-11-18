from django import forms

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