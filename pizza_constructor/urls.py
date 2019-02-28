from django.urls import path
from . import views

urlpatterns = [
    path('', views.constructor_page, name='constructor_page'),
    path('order/<int:pk>', views.order_page, name='order_page'),
]