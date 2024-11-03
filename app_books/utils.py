from django.db.models import Q

from .models import Books, Tag


def search_thing(search_query):

    tag = Tag.objects.filter(name__icontains=search_query)
    
    books = Books.objects.filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tags__in=tag)
    )

    return books, search_query