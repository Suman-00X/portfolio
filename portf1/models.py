

from pyexpat import model

from django.forms import CharField


class user(model.Model):
    name =CharField(max_length=100)
    role =CharField(max_length=100)