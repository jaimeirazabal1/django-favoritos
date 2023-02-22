from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index_favoritos(request):
    return render(request, 'favoritos/lista.html')

def crear_favoritos(request):
    # form = FavoritoForm()
    form = FavoritoModelForm()
    
    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre']
            # url = form.cleaned_data['url']
            # favorito = Favoritos(nombre=nombre, url=url)
            # favorito.save()
            form.save()
        else:
            print(form.errors)
        # Favoritos.objects.create(nombre=nombre, url=url) se puede asi
    
        
    return render(request, 'favoritos/crear.html',{"form":form})

def lista_favoritos(request):
    favoritos = Favoritos.objects.all()
    print(favoritos.query)
    return render(request, 'favoritos/lista.html',{"favoritos":favoritos})