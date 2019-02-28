from django import forms
from .models import Order


class OrderIngredientsForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('dough_type', 'text',)
