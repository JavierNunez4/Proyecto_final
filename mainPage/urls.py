from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

app_name ="main"#aqui se le regitra un nombre globlal a esta seccion de urls en la aplicacion para poder llamarla 
                #en otro archivo de manera especifica
urlpatterns = [
    path("", views.main, name="main"),
    path("registrar/", views.registrar, name="register"),
    path('login/', views.login.as_view(template_name='mainPage/login.html', success_url='/account/'), name="login"),#aqui llamamos a la vista login default de django y a la logout
    path("logout/", LogoutView.as_view(template_name='mainPage/logout.html',next_page='/login/'), name="logout"),
    path("account/", views.cuentaUser, name="account"),
    path("solicitud/", login_required(views.solicitud), name="solicitud"),
    path("adminsolicitud/", login_required(views.solicitudAdmin), name="solicitudAdmin"),
    path("borrar/<int:pk>", login_required(views.rechazar), name="eliminar"),
    path("solidetail/<int:pk>", login_required(views.soliDetalles), name="solidetail"),
    path("aceptar/<int:pk>", login_required(views.aceptar), name="aceptar"),
    
]
#la funcion login_required agrega la seguridad de que el usuario deba estar logeado para poder ingresar a esa url