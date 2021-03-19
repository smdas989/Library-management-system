from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Student, Faculty, Admin, Librarian
from django.conf import settings 
from django.core.mail import send_mail 
import datetime
@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        #Sending email to the user
        subject = 'You have been registered'
        message = f'Hi,{instance.username} thank you for registering in Library management system.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = ['smdas989@gmail.com', ] 
        send_mail( subject, message, email_from, recipient_list, fail_silently=False, ) 
    elif instance:
        date1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if str(instance.last_login)[:16] != date1:
            subject = 'Profile Updation'
            message = f'Hi,{instance.username} you profile has been successfully updated in Library management system.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['smdas989@gmail.com', ] 
            send_mail( subject, message, email_from, recipient_list, fail_silently=False, )         
   