from django.shortcuts import render, redirect
from .models import Order, OrderItem
from menu.models import Dish

def take_order(request):
    dishes = Dish.objects.all()

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        order = Order.objects.create(customer_name=customer_name)

        for dish in dishes:
            quantity = int(request.POST.get(f'dish_{dish.id}', 0))
            if quantity > 0:
                OrderItem.objects.create(order=order, dish=dish, quantity=quantity)

        return redirect('order_list')

    return render(request, 'orders/take_order.html', {'dishes': dishes})


def order_list(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        order_id = int(request.POST['order_id'])
        new_status = request.POST['new_status']
        order = Order.objects.get(pk=order_id)
        order.status = new_status
        order.save()

    return render(request, 'orders/order_list.html', {'orders': orders})