from django.db import models
from typing import List


class IngredientGroup(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price: float = models.FloatField()
    group = models.ForeignKey(IngredientGroup, related_name="ingredients",
                              on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.group, self.price)


class Order(models.Model):
    dough_type = models.CharField(max_length=6)
    email = models.EmailField("Ваш email")
    phone = models.CharField("Ваш номер телефона", max_length=20)
    name = models.CharField("Ваше имя", max_length=100)
    amount = models.FloatField("Сумма заказа: ", default=0)
    confirmed = models.BooleanField(default=False)
    objects = models.Manager()

    @property
    def dough_type_string(self):
        if self.dough_type == 'white':
            return "белое"
        else:
            return "черное"

    @property
    def price(self):
        total_price = 0
        order_ingredients: List[OrderIngredient] = self.__getattribute__("ingredients").all()
        for order_ingredient in order_ingredients:
            total_price += order_ingredient.quantity * order_ingredient.ingredient.price
        return total_price


class OrderIngredient(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="ingredients")
    ingredient: Ingredient = models.ForeignKey(Ingredient,
                                               on_delete=models.CASCADE)
    quantity: float = models.IntegerField(default=1)
    objects = models.Manager()

    @property
    def price(self):
        return self.ingredient.price * self.quantity

    class Meta:
        unique_together = ('order', 'ingredient')
