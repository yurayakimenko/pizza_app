from django.contrib import admin
from .models import Ingredient, IngredientGroup, Order, OrderIngredient


class OrderIngredientInline(admin.TabularInline):
    model = OrderIngredient
    fk_name = "order"


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderIngredientInline,
    ]


admin.site.register(Ingredient)
admin.site.register(IngredientGroup)
admin.site.register(OrderIngredient)
admin.site.register(Order, OrderAdmin)
