from .models import Order, OrderItem

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created and instance.status == 'accepted':
        customer = instance.customer
        print(list(customer.order_set.all()))
        try:
            order_id = list(customer.order_set.all())[-2].id
        except:
            order_id = list(customer.order_set.all())[0].id
                
        order = Order.objects.get(id=order_id)
        order_items = order.orderitem_set.all()
        
        subject = 'Potwierdzenie zamówienia'
        html_content = render_to_string('emails/order_confirmation_email.html', {'customer': customer, 'order': order, 'order_items': order_items, 'order_id': order_id})
        text_content = strip_tags(html_content)

        from_email = settings.EMAIL_HOST_USER
        to_email = [customer.email]
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@receiver(post_save, sender=Order)
def send_order_status_update_email(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.status == 'accepted':
        customer = instance.customer
        order = instance
        order_items = order.orderitem_set.all()
        
        subject = 'Aktualizacja statusu zamówienia'
        html_content = render_to_string('emails/order_status_update_email.html', {'customer': customer, 'order': order, 'order_items': order_items})
        text_content = strip_tags(html_content)

        from_email = settings.EMAIL_HOST_USER
        to_email = [customer.email]
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
