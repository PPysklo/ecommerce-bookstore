from .models import Profile, User

from django.db.models.signals import post_save, post_delete
from django.conf import settings
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
        )
        
        subject = 'Witamy na naszej stronie!'
        html_content = render_to_string('emails/welcome_email.html')
        text_content = strip_tags(html_content)

        from_email = settings.EMAIL_HOST_USER
        to_email = [profile.email]
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        

@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.email = profile.email
        user.save()
        
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
    


