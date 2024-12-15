from django.urls import path
from . import views

app_name = 'app_books'

urlpatterns = [
    path("", views.books_list, name='books-list'),
    path('book/<str:pk>', views.BookDetailView.as_view(), name='book-detail'),
    
    path("shooping-cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path("update_item/", views.updateitem, name='update-item'),
    
]
