from django.db import models
from menu.models import MenuItem


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    min_quantity = models.IntegerField(default=0)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)  # example : GR, LITR , NUMBERS
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipes')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient.name} در {self.menu_item.name} "
