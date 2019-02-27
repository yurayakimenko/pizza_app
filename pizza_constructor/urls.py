from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_constructor_page, name='constructor_page'),
    # path('contacts', views., name='constructor_page'),
]