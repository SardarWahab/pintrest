
from django.contrib import admin
from django.urls import path
from .views import *
from pin import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('create/',create),
    path('profile/',profile),
    path('login/',app_views.handle_login,name='login'),
    path('register/',app_views.handle_register,name='register')
]
