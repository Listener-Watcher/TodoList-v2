from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise forms.ValidationError("Please use a valid email address.")
        return email
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise forms.ValidationError("Please use a valid email address.")
        return email
