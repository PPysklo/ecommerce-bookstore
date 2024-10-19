from django.urls import path
from . import views

app_name = 'app_books'

urlpatterns = [
    path("", views.home, name='home')
]