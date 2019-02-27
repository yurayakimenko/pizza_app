from django.shortcuts import render


def pizza_constructor_page(request):
    return render(request, 'pizza_constructor/constructor_form.html', {})

