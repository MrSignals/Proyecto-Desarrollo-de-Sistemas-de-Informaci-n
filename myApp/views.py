from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.
def home(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedor.html',{
        "proveedor": proveedor
    })

def registrarProveedor(request):
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    proveedor = Proveedor.objects.create(nombre = nombre, direccion = direccion, telefono = telefono)
    return redirect('/')

def products(request):
    return render(request, 'products.html')
