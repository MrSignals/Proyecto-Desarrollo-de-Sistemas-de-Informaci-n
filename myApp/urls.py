from django.urls import path
from . import views

urlpatterns = [
   path('', views.signin, name='signin'),
   path('signup/', views.signup),
   path('proveedor/', views.proveedor),
   path('registrarProveedor/', views.registrarProveedor),
   path('eliminarProveedor/<codigo>',views.eliminarProveedor),
   path('edicionProveedor/<codigo>', views.edicionProveedor),
   path('editarProveedor/', views.editarProveedor)
]