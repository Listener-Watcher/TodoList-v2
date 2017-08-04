from django.test import TestCase

# Create your tests here.
class NewUser(models.Model):
    email = models.EmailField()
    name = model.CharField()
    time = model.DateTimeField(auto_now_add=True, auto_now=False)
    updated = model.DateTimeField(auto_now_add=False, auto_now=True)
