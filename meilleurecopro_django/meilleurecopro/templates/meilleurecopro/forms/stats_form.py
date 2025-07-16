from django import forms

class StatsForm(forms.Form):
    OPTIONS = [
        ('city', 'Ville'),
        ('department', 'Département'),
        ('zip_code', 'Code Postal'),
    ]

    location_type = forms.ChoiceField(
        choices=OPTIONS,
        widget=forms.RadioSelect,
        label="Choisir un type de localisation"
    )
    location = forms.CharField(
        max_length=100,
        label="location",
        widget=forms.TextInput(attrs={'placeholder': 'Saisir texte...'})
    )