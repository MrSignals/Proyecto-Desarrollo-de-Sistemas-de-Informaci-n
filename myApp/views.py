from django.shortcuts import render, redirect
from .models import Proveedor
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def proveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedor.html',{
        "proveedor": proveedor
    })

def signup(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['correo']
        contraseña1 = request.POST['contraseña1']
        contraseña2 = request.POST['contraseña2']
        
        myuser = User.objects.create_user(usuario,email,contraseña1)
        myuser.first_name = nombre
        myuser.last_name = apellido
        
        myuser.save()
        
        messages.success(request, "Cuenta creada con exito")
        return redirect('signin')
    
    return render(request,'signup.html')


def signin(request):
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')

def registrarProveedor(request):
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    codigo = request.POST['codigo']
    proveedor = Proveedor.objects.create(nombre = nombre, direccion = direccion, telefono = telefono ,codigo_proveedor = codigo)
    return redirect('/proveedor')

def eliminarProveedor(request,codigo):
    proveedor = Proveedor.objects.get(codigo_proveedor = codigo)
    proveedor.delete()
    return redirect('/proveedor')

def edicionProveedor(request, codigo):
    proveedor = Proveedor.objects.get(codigo_proveedor = codigo)
    return render(request, 'edicionProveedor.html', {"proveedor": proveedor})

def editarProveedor(request):
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    codigo = request.POST['codigo']
    
    proveedor = Proveedor.objects.get(codigo_proveedor = codigo)
    proveedor.nombre = nombre
    proveedor.direccion = direccion
    proveedor.telefono = telefono
    proveedor.save()
    
    return redirect('/proveedor')
    
def products(request):
    return render(request, 'products.html')
