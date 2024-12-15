import uuid

from app_users.models import Profile

from django.db import models


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
    
class OrderItem(models.Model):
    book = models.ForeignKey(Books, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)
    country = models.CharField(max_length=200, null = True)
    postal_code = models.CharField(max_length=200, null = True)
    telephone = models.CharField(max_length=200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.order}----{self.address}"

