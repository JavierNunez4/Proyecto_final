from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.main, name="main"),
    path("registrar/", views.registrar, name="register"),
    path('login/', LoginView.as_view(template_name='mainPage/login.html', success_url='/account/'), name="login"),
    path("logout/", LogoutView.as_view(template_name='mainPage/logout.html',next_page='/login'), name="logout"),
    path("account/", views.cuentaUser, name="account"),
    path("solicitud/", views.solicitud, name="solicitud"),
    path("adminsolicitud/", views.solicitudAdmin, name="solicitudAdmin"),
    
    
]