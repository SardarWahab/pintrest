
from django.contrib import admin
from django.urls import path
from .views import *
from pin import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('create/',app_views.create_pin),
    path('profile/',app_views.my_profile),
    path('login/',app_views.handle_login,name='login'),
    path('register/',app_views.handle_register,name='register'),
    path('logout/',app_views.handle_logout),
    path('pin/<int:id>',app_views.single_pin, name='pin'),
    path('delete-pin/<int:id>',app_views.delete_pin),
    path('update-pin/<int:id>',app_views.update_pin),
    path('save-pin/<int:id>', app_views.save_pin,name='save-pin')
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 