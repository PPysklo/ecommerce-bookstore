from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Books, Tag


def search_thing(search_query, books=None):

    tag = Tag.objects.filter(name__icontains=search_query)
    
    if books is not None:
        books = Books.objects.filter(
            Q(title__icontains=search_query) |
            Q(tags__in=tag) |
            Q(author__icontains=search_query)
        ).distinct()

    return books, search_query

def paginateBooks(request, books, results):
    page = request.GET.get('page')
    paginator = Paginator(books,results)
  
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        books = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        books = paginator.page(page)
        
    leftIndex = (int(page) - 4)
    
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex,rightIndex)
        
    return custom_range, books

