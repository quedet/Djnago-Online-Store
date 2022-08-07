from django.shortcuts import render

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from .tasks import order_created

# Create your views here.
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            #clear the cart
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'order/create.html', {'form': form, 'cart': cart })