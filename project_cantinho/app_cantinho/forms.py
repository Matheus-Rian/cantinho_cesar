from django import forms

class OptionsVendinha(forms.Form):
	options = (
			('BRUM', 'BRUM'),
			('TIRADENTES', 'TIRADENTES'),
			('APOLLO', 'APOLLO'),
	)
	choices = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
