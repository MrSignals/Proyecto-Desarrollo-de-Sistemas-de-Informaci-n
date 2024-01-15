from django.urls import path
from . import views

urlpatterns = [
   path('', views.signin, name='home'),
   path('signin/', views.signin, name='signin'),
   path('signup/', views.signup),
   path('proveedor/', views.proveedor, name= "proveedor"),
   path('productos/', views.products, name="productos"),
   path('registrarProveedor/', views.registrarProveedor),
   path('eliminarProveedor/<codigo>',views.eliminarProveedor),
   path('edicionProveedor/<codigo>', views.edicionProveedor),
   path('editarProveedor/', views.editarProveedor)
]