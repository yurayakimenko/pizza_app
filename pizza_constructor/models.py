from django.db import models


class IngredientGroup(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    group = models.ForeignKey(IngredientGroup, related_name="ingredients",
                              on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.group, self.price)


class Order(models.Model):
    dough_type = models.CharField(max_length=6)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    confirmed = models.BooleanField(default=False)
    objects = models.Manager()


class OrderIngredient(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __init__(self, order, ingredient, quantity):
        self.order = order
        self.ingredient = ingredient
        self.quantity = quantity

    class Meta:
        unique_together = ('order', 'ingredient')
