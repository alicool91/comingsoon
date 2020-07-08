from django.db import models
from django.forms import ModelForm

# Create your models here.

class Users(models.Model):
	name = models.TextField()
	email = models.EmailField(max_length = 254)


