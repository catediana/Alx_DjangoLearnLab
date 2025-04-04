from django import forms
from django import forms

class ExampleForm(forms.Form):
    # Define the fields for your form here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
