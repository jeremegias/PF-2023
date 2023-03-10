"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from travel_blog_app.views import index, PostList, PostBorrar, PostDetalle, PostActualizar, PostCrear, UserSignUp, UserLogin, UserLogout, AvatarActualizar,UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar, MensajeBorrar, AboutView
from django.contrib.admin.views.decorators import staff_member_required 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel_blog_app/', index, name="travel_blog_app_index"),
    path('travel_blog_app/about/', AboutView.as_view(), name="travel_blog_app_about"),
    path('travel_blog_app/<int:pk>/detalle/', PostDetalle.as_view(), name="travel_blog_app_detalle"),
    path('travel_blog_app/listar', PostList.as_view(), name="travel_blog_app_listar"),
    path('travel_blog_app/crear', PostCrear.as_view(), name="travel_blog_app_crear"),
    path('travel_blog_app/<int:pk>/borrar/', PostBorrar.as_view(), name="travel_blog_app_borrar"),
    path('travel_blog_app/<int:pk>/actualizar/', PostActualizar.as_view(), name="travel_blog_app_actualizar"),
    path('travel_blog_app/signup/', UserSignUp.as_view(), name ="travel_blog_app_signup"),
    path('travel_blog_app/login/', UserLogin.as_view(), name="travel_blog_app_login"),
    path('travel_blog_appp/logout/', UserLogout.as_view(), name = "travel_blog_app_logout"),
    path('travel_blog_app/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="travel_blog_app_avatars_actualizar"),
    path('travel_blog_app/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="travel_blog_app_users_actualizar"),    
    path('travel_blog_app/mensajes/crear/', MensajeCrear.as_view(), name="travel_blog_app_mensajes_crear"),
    path('travel_blog_app/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="travel_blog_app_mensajes_borrar"),
    path('travel_blog_app/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="travel_blog_app_mensajes_detalle"),
    path('travel_blog_app/mensajes/listar/', MensajeListar.as_view(), name="travel_blog_app_mensajes_listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
