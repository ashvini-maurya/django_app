from django import forms
from autofill.models import User

class UserForm(forms.ModelForm):
  city = forms.CharField(max_length=128, help_text="Enter City Name.")
  state = forms.CharField(max_length=128, help_text="Enter/Select State Name.")
  country = forms.CharField(max_length=128, help_text="Enter/Select Country Name.")

  class Meta:
    model = User
    