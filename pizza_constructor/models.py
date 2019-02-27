from django.db import models


class IngredientGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    group = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.group, self.price)


class Order(models.Model):
    dough_type = models.CharField(max_length=6)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
