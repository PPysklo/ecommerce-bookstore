from django.urls import path
from . import views

app_name = 'app_books'

urlpatterns = [
    path("", views.books_list, name='books-list'),
    path("shooping-cart/", views.cart, name='cart'),
    path('book/<str:pk>', views.BookDetailView.as_view(), name='book-detail')
]