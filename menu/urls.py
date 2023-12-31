from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.dish_list, name='dish_list'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('edit_dish/<int:dish_id>/',views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),

]
