from .models import Tag, Order

def tags_processor(request):
    tags = Tag.objects.all()
    return {'tags': tags}

def cart_items_processor(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = len(order.orderitem_set.all())
    else:
        items = []
        
    return {'cartitems':items}

def uncompleted_orders_processor(request):
    uncompleted_orders_count = Order.objects.filter(is_fulfilled=False).exclude(transaction_id__isnull=True).count()

    return {'uncompleted_orders_count': uncompleted_orders_count}