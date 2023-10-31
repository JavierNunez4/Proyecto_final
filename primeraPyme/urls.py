from django.urls import path
from . import views
urlpatterns = [
    path("", views.pyme1, name="pyme1"),
    path("crear/", views.GuardarProducto.as_view(), name="crear_producto"),
    path("<int:pk>", views.detalles, name="detalle"),
]