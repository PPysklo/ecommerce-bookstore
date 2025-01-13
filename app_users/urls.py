from django.urls import path
from . import views

app_name = 'app_users'

urlpatterns = [
    path('login_Register/',views.loginRegister,name="login-register"),
    path('logout/',views.logOut, name='logout'),
    path('profile/', views.profile, name='profile'),
    path("edit_profile/<str:pk>", views.edit_profile, name="edit-profile"),
    path('statute/', views.statute, name='statute'),
]