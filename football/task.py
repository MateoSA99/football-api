# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_registration_email(email):
    subject = '¡Bienvenido a nuestra API!'
    message = 'Gracias por registrarte en nuestra API. ¡Disfruta de nuestras características!'
    sender = "mateosarango99@gmail.com"
    recipient_list = [email]
    
    send_mail(subject, message,sender,recipient_list)

@shared_task
def send_login_email(email):
    subject = '¡Has Iniciado sesión a nuestra API!'
    message = 'Gracias por iniciar sesión en nuestra API. ¡Disfruta de nuestras características!'
    sender = "mateosarango99@gmail.com"
    recipient_list = [email]
    
    send_mail(subject, message,sender,recipient_list)

