from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Books, Tag


def home(request):
    
    return render(request,'index.html')
    

def books_list(request):
    books = Books.objects.all()
    tags = Tag.objects.all()
    
    # if request.GET.get('category'):
    #     category_name = request.GET['category']

    #     category_tag = get_object_or_404(Tag, name=category_name)

    #     books = books.filter(tags=category_tag)

   
  
    # custom_range, books = paginateProjects(request, books, 8)
    
    # if request.user.is_authenticated:
    #     customer = request.user.profile
    #     order, created = Order.objects.get_or_create(customer = customer, complete = False)
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     items = []
    #     order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}
    #     cartItems = order['get_cart_items']
        
    
    context = {
        'books' : books,
        'tags' : tags,
        # 'cartitems' : cartItems,
        # 'search_query' : search_query,
        # 'custom_range' : custom_range,
    }
    
    return render(request,'app_books/books_list.html', context)

def cart(request):
    # if request.user.is_authenticated:
    #     customer = request.user.profile
    #     order, created = Order.objects.get_or_create(customer=customer, complete = False)
    #     items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total':0 , 'get_cart_items':0}
        
    # context = {'items':items, 'order': order}
    return render(request, 'shooping_cart.html')