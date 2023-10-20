from django.urls import path
from . import views
urlpatterns = [
    path("", views.pyme1, name="pyme1"),
]