import uuid

from app_users.models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length= 100, default = None)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places  = 2, default = None)
    tags = models.ManyToManyField('Tag',blank=True)
    image = models.ImageField(upload_to='images/',null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    stock = models.PositiveIntegerField(default=0) 
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['id']


    @property
    def imageURL(self):
        try:
            url = self.image.url            
        except:
            url = ''
   
        return url
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    order_date = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default= False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    class Meta:
        permissions = [
            ('can_change_order', 'Can change order'),
            ('can_delete_order', 'Can delete order'),
            ('can_view_order', 'Can view order'),
        ]
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_all_cart_items(self):
        orderitems = self.orderitem_set.all()
        all_items = [item.quantity for item in orderitems]
        return all_items
    
class OrderItem(models.Model):
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        permissions = [
            ('can_add_order_item', 'Can add order item'),
            ('can_change_order_item', 'Can change order item'),
            ('can_delete_order_item', 'Can delete order item'),
            ('can_view_order_item', 'Can view order item'),
        ]
    
    def __str__(self):
        return f"Numer zamówienia: {str(self.order.id)}"

    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total

    def clean(self):
        if self.book and self.quantity > self.book.stock:
            raise ValidationError(f"Not enough stock for {self.book.title}. Available: {self.book.stock}, requested: {self.quantity}")

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)
    country = models.CharField(max_length=200, null = True)
    postal_code = models.CharField(max_length=200, null = True)
    telephone = models.CharField(max_length=200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        permissions = [
            ('can_add_shipping_address', 'Can add shipping address'),
            ('can_change_shipping_address', 'Can change shipping address'),
            ('can_delete_shipping_address', 'Can delete shipping address'),
            ('can_view_shipping_address', 'Can view shipping address'),
        ]

    def __str__(self):
        return f"{self.order}----{self.address}"

@receiver(post_save, sender=Order)
def update_stock_on_order_complete(sender, instance, **kwargs):
    if instance.complete:
        for item in instance.orderitem_set.all():
            item.book.stock -= item.quantity
            item.book.save()

@receiver(post_delete, sender=OrderItem)
def update_stock_on_delete(sender, instance, **kwargs):
    if instance.order.complete:
        instance.book.stock += instance.quantity
        instance.book.save()