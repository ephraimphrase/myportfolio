from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from .models import Message
from myportfolio.settings import EMAIL_HOST_USER as admin_mail

@shared_task
def send_message_email(id, email, message, subject):
    
    message = Message.objects.get(id=id)

    mail_sent = send_mail(
        subject=subject,
        message = message,
        from_email=admin_mail,
        recipient_list=[email],
        fail_silently=False
    )

    return mail_sent