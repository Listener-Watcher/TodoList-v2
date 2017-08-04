from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'priority', 'text']
    def clean_title(self):
        title = self.cleaned_data.get('title').encode('utf-8')
        if len(title) > 120:
            raise forms.ValidationError("Length of title should be less than 120.")
        return title
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        return deadline
    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        return priority
    def clean_text(self):
        text = self.cleaned_data.get('text')
        return text




# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = SignUp
#         fields = ['full_name', 'email']
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not "@" in email:
#             raise forms.ValidationError("Please use a valid email address.")
#         return email
