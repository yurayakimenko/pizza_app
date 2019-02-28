from ... import models
from django.core.management.base import BaseCommand
from random import uniform

ingredient_groups = {
    "Мясо": ["Свинина", "Салями", "Баранина"],
    "Птица": ["Индюк", "Курица", "Утка"],
    "Овощи": ["Грибы", "Перец болгарский"]
}


class Command(BaseCommand):
    help = 'Initialize database'

    def handle(self, *args, **kwargs):
        for group_name, ingredients in ingredient_groups.items():
            group = models.IngredientGroup.objects.create(name=group_name)
            for ingredient_name in ingredients:
                models.Ingredient.objects.create(name=ingredient_name,
                                                 group=group,
                                                 price=round(uniform(1, 10), 1))
        self.stdout.write("Database initialization has done!")
