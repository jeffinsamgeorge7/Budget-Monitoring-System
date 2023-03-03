from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('a/', admin.site.urls),
    path('admin/',include('administrator.urls')),
    path('',include('userapp.urls')),
    path('auth/',include('accounts.urls'))
]
