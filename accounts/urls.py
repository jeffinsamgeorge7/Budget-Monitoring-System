from accounts.views import Loginview, logout_view
from django.urls import path

urlpatterns = [
    path('login/',Loginview.as_view(),name="loginpage"),
    path('logout/',logout_view,name="logoutpage")
]
