from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.take_order, name='take_order'),
    path('list/', views.order_list, name='order_list'),

]
