import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Books, Tag, Order, OrderItem
from .utils import search_thing, paginateBooks

class BookDetailView(DetailView):
    model = Books

def books_list(request):
    books = Books.objects.all()
    tags = Tag.objects.all()
    category_tag = None
    
    if request.GET.get('category'):
        category_name = request.GET['category']

        category_tag = get_object_or_404(Tag, name=category_name)

        books = books.filter(tags=category_tag)
        
    query = request.GET.get('search_query', '')
    if query:
        books, search_query = search_thing(query, books)

    
    custom_range, books = paginateBooks(request, books, 12)
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}
        cartItems = order['get_cart_items']
        
    
    context = {
        'books' : books,
        'tags' : tags,
        'cartitems' : cartItems,
        'custom_range' : custom_range,
        'category_tag' : category_tag,
    }
    
    return render(request,'app_books/books_list.html', context)

# SHOOPING CART SECTION

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
        
    context = {'items':items, 'order': order}
    return render(request, 'shooping_cart.html', context)

def updateitem(request):
    data = json.loads(request.body)
    productId = data['bookId']
    action = data['action']

    
    customer = request.user.profile
    book = Books.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, book = book)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

@csrf_exempt  
def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}

    context = {'items':items, 'order': order}
    return render(request, 'stuff/checkout.html', context)