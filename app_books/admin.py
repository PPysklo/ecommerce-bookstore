from django.contrib import admin
from .models import Order, OrderItem, Books

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'is_fulfilled', 'customer', 'transaction_id', 'order_date')
    list_filter = ('complete', 'order_date')
    inlines = [OrderItemInline]

    actions = ['is_fulfilled', 'ship_order']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(transaction_id__isnull=True)

    def is_fulfilled(self, request, queryset):
        queryset.update(is_fulfilled=True)
        self.message_user(request, "Selected orders have been marked as complete.")
    is_fulfilled.short_description = "Mark selected orders as complete"

    def ship_order(self, request, queryset):
        queryset.update(shipped=True)
        self.message_user(request, "Selected orders have been shipped.")
    ship_order.short_description = "Ship selected orders"

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'date_added')
    
@admin.register(Books)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')