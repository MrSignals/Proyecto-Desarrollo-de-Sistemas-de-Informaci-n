from django.db import models


class Proveedor(models.Model):
    codigo_proveedor = models.CharField(max_length=20, unique=True, default="")
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class ComponenteElectronico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    numero_de_serie = models.CharField(max_length=50, unique=True)
    cantidad_disponible = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_de_ingreso = models.DateField(auto_now_add=True)
    fecha_de_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

 

                                  



