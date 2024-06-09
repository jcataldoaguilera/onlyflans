from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    pub = { 'flanes_publicos' : flanes_publicos }
    return render(request,"index.html",pub)

def acerca(request):
    return render(request,"about.html",{})

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    priv = { 'flanes_privados' : flanes_privados }
    return render(request,"welcome.html",priv)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request,"contact.html",{'form' : form})

def exito(request):
    return render(request,"success.html",{})