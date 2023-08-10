from django.shortcuts import render, redirect
from .models import Dish

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        availability = request.POST.get('availability', False)=='on'
        Dish.objects.create(name=name, price=price, availability=availability)
        return redirect('dish_list')  # Redirect to dish list after adding a dish
    return render(request, 'menu/add_dish.html')

def edit_dish(request,dish_id):
    dish = Dish.objects.get(pk=dish_id)
  
    if request.method == 'POST':
        dish.name = request.POST['name']
        dish.price = request.POST['price']
        dish.availability = request.POST.get('availability') =='on'

        dish.save()
        return redirect('dish_list')

    return render(request, 'menu/edit_dish.html', {'dish': dish})

def delete_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)

    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')

    return render(request, 'menu/confirm_delete_dish.html', {'dish': dish})
