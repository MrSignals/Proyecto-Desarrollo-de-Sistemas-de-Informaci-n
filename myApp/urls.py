from django.urls import path
from . import views

urlpatterns = [
   path('', views.signin, name='home'),
   path('signin/', views.signin, name='signin'),
   path('signup/', views.signup),
   path('signout/', views.signout, name="signout"),
   path('proveedor/', views.proveedor, name= "proveedor"),
   path('productos/', views.products, name="productos"),
   path('registrarProveedor/', views.registrarProveedor),
   path('registrarProducto/',views.registrarProducto),
   path('eliminarProveedor/<codigo>', views.eliminarProveedor),
   path('edicionProveedor/<codigo>', views.edicionProveedor),
   path('edicionProducto/<numero_de_serie>/', views.edicionProducto, name='edicionProducto'),
   path('eliminarProducto/<numero_de_serie>/', views.eliminarProducto),
   path('editarProducto/', views.editarProducto),
   path('editarProveedor/', views.editarProveedor),
]