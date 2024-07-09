from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .models import Flan, ContactForm
from .forms import ContactFormModelForm,RegistrationForm

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    pub = { 'flanes_publicos' : flanes_publicos }
    return render(request,"index.html",pub)

def acerca(request):
    return render(request,"about.html",{})

@login_required(redirect_field_name="/accounts/login/")
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    priv = { 'flanes_privados' : flanes_privados }
    return render(request,"welcome.html",priv)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = form.save()
            return redirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request,"contact.html",{'contact' : form})

def exito(request):
    return render(request,"success.html",{})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/bienvenido')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'registration' : form})