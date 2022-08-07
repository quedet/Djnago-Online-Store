# from celery import shared_task

from django.core.mail import send_mail
from orders.models import Order
from myshop.celery import app

@app.task
def order_created(order_id):
    """
    Task to send e-mail notification when the order is successfully created.
    """

    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name}, \n\nYou have successfully place an order. \nYour order ID is {order.id}"
    mail_sent = send_mail(subject, message, 'admin@gmail.com', [order.email])

    return mail_sent