from django.shortcuts import render, redirect, get_object_or_404
from .models import IngredientGroup, Order, OrderIngredient, Ingredient
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .forms import OrderForm
from django.conf import settings
from django.core.mail import send_mail


@csrf_protect
def constructor_page(request):
    if request.method == "POST":
        order = Order()
        order.save(force_insert=True)
        for key, value in request.POST.items():
            if 'dough_type' in key:
                order.dough_type = value
                order.save()
            elif 'ingredient_amount' in key:
                ingredient = Ingredient.objects.get(id=int(key.split('ingredient_amount_')[1]))
                quantity = int(value)
                if quantity > 0:
                    OrderIngredient.objects.create(order=order, ingredient=ingredient,
                                                   quantity=quantity)
        return redirect('order_page', pk=order.pk)
    else:
        ingredient_groups = IngredientGroup.objects.all()
        return render(request, 'pizza_constructor/constructor_form.html',
                      {"title": "Выбери ингредиенты пиццы",
                       "ingredient_groups": ingredient_groups},
                      RequestContext(request))


def order_page(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
        email_text = "Вы оформили заказ пиццы №{} на сумму {}$".format(order.pk, order.price)
        send_mail(
            'Новый заказ №{}'.format(order.pk),
            email_text,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
        )
        return redirect('order_page', pk=order.pk)
    else:
        order_form = OrderForm()
        return render(request, 'pizza_constructor/order_form.html',
                      {"form": order_form,
                       "order": order})

