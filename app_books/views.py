from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import JsonResponse

from .models import Books, Tag
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

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        if query:
            if len(query) >= 3:
                things, search_query = search_thing(query, things)

        results = [
                {
                    'id': thing.id,
                    'name': thing.name,
                    'owner': thing.owner.username,
                    'location': thing.location.name if thing.location else "",
                    'image': thing.image_set.first().image.url if thing.image_set.exists() else None
                }
                for thing in things
            ]

        return JsonResponse(results, safe=False)
  
    custom_range, books = paginateBooks(request, books, 8)
    
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
        'custom_range' : custom_range,
        'category_tag' : category_tag,
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

