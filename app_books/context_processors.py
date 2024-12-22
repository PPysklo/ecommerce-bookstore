from .models import Tag, Order

def tags_processor(request):
    tags = Tag.objects.all()
    return {'tags': tags}

def uncompleted_orders_processor(request):
    uncompleted_orders_count = Order.objects.filter(is_fulfilled=False).exclude(transaction_id__isnull=True).count()

    return {'uncompleted_orders_count': uncompleted_orders_count}