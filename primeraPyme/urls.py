from django.urls import path
from . import views

app_name="gestion"
urlpatterns = [
    path("", views.pyme1, name="pyme1"),
    path("crear/", views.GuardarProducto.as_view(), name="crearProducto"),
    path("<int:pk>", views.detalles, name="detalle"),
]