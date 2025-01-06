from django.contrib import admin
from django import forms
from .models import Order, OrderItem, Books, Tag

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('__str__', 'id', 'is_fulfilled', 'customer', 'transaction_id', 'order_date')
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
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'complete' in form.base_fields:
            form.base_fields['complete'].widget = forms.HiddenInput()
        return form

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'date_added')
    
@admin.register(Books)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)