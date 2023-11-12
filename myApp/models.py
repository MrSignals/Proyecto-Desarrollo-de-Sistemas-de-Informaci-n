from django.db import models

# Create your models here.
from django.db import models

class Informe(models.Model):
    cod_informe = models.CharField(max_length=15, unique=True)
    reseñas_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    productos_comprado = models.CharField(max_length=100)
    fecha_informe = models.DateField()
class Compra(models.Model):
    cod_compra = models.CharField(max_length=15, unique=True)
    cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateField()
    forma_pago = models.CharField(max_length=50)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)
    pais = models.CharField(max_length=100)
class Producto(models.Model):
    cod_producto = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    proveedor = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
class Resena(models.Model):
    cod_resena = models.CharField(max_length=15, unique=True)
    calificacion = models.PositiveIntegerField()
    reseña = models.TextField()
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()



                                  



