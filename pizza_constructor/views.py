from django.shortcuts import render, redirect
from .models import IngredientGroup, Order, OrderIngredient, Ingredient
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def constructor_page(request):
    if request.method == "POST":
        print(request.POST)
        order = Order()
        for key, value in request.POST:
            if 'dough_type' in key:
                order.dough_type = value[0]
            elif 'ingredient_amount' in key:
                ingredient = Ingredient.objects.get(id=int(key.split('ingredient_amount_')[0]))
                order_ingredient = OrderIngredient(order, ingredient, int(value[0]))
                order_ingredient.save()
        order.save()
        return redirect('order_page')
    else:
        ingredient_groups = IngredientGroup.objects.all()
        return render(request, 'pizza_constructor/constructor_form.html',
                      {"title": "Выбери ингредиенты пиццы",
                       "ingredient_groups": ingredient_groups},
                      RequestContext(request))


def order_page(request):
    pass

