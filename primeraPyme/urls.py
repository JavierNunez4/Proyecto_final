from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name="gestion"
urlpatterns = [
    #path("", views.pyme1, name="pyme1"),
    path("pyme<int:pk>", views.pyme1, name="pyme"),
    path("agregar/<int:pk>", login_required(views.GuardarProducto.as_view()), name="agregarProducto"),
    path("producto/<int:pk>", views.detalles, name="detalle"),#el <int:pk> sirve para decirle a la url que se espera un dato entero 
    #esto sirve para poder ver datos especificos de un campo en la bd

    
]
   