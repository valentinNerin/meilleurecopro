from django import forms

class AddEstateForm(forms.Form):
    estate_url = forms.CharField(
        max_length=200,
        label="url",
        widget=forms.TextInput(attrs={'placeholder': 'Saisir texte...'})
    )