from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_fname', 'customer_lname', 'message']
        labels = {
            'customer_fname' : 'Nombre',
            'customer_lname' : 'Apellido',
            'customer_email' : 'Correo',
            'message' : 'Mensaje',
            }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']