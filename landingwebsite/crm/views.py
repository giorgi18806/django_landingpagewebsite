from django.shortcuts import render
from .models import Order
from .forms import OrderForm


def first_page(request):
    orders = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'orders': orders, 'form': form})


def thanks_page(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thanks-page.html', {"name": name, "phone": phone})