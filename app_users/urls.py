from django.urls import path
from . import views

app_name = 'app_users'

urlpatterns = [
    path('login_Register/',views.loginRegister,name="login_Register"),
    path('logout/',views.logOut, name='logout'),
]