from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Dish Name: {self.name} - ({'' if self.availability else 'Not '}Available)"

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='received')

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
