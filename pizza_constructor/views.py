from django.shortcuts import render
from .models import IngredientGroup


def pizza_constructor_page(request):
    ingredient_groups = IngredientGroup.objects.all()
    return render(request, 'pizza_constructor/constructor_form.html',
                  {"title": "Выбери ингредиенты пиццы",
                   "ingredient_groups": ingredient_groups})

