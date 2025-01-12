from django.contrib import admin
from django import forms
from .models import Order, OrderItem, Books, Tag

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'status', 'is_fulfilled', 'customer', 'transaction_id', 'order_date')
    list_filter = ('status', 'order_date')
    inlines = [OrderItemInline]

    actions = [
        'mark_as_fulfilled', 
        'ship_order', 
        'mark_as_accepted', 
        'mark_as_in_progress', 
        'mark_as_delivered', 
        'mark_as_cancelled'
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(transaction_id__isnull=True)

    def mark_as_fulfilled(self, request, queryset):
        queryset.update(is_fulfilled=True)
        self.message_user(request, "Selected orders have been marked as fulfilled.")
    mark_as_fulfilled.short_description = "Mark selected orders as fulfilled"

    def ship_order(self, request, queryset):
        queryset.update(status='shipped')
        self.message_user(request, "Selected orders have been shipped.")
    ship_order.short_description = "Ship selected orders"

    def mark_as_accepted(self, request, queryset):
        queryset.update(status='accepted')
        self.message_user(request, "Selected orders have been marked as accepted.")
    mark_as_accepted.short_description = "Mark selected orders as accepted"

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, "Selected orders have been marked as in progress.")
    mark_as_in_progress.short_description = "Mark selected orders as in progress"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='delivered')
        self.message_user(request, "Selected orders have been marked as delivered.")
    mark_as_delivered.short_description = "Mark selected orders as delivered"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, "Selected orders have been marked as cancelled.")
    mark_as_cancelled.short_description = "Mark selected orders as cancelled"


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'complete' in form.base_fields:
            form.base_fields['complete'].widget = forms.HiddenInput()
        return form

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'date_added')

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)