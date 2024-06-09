from django.shortcuts import render
from .models import Flan

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