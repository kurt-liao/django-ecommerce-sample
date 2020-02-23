from django.urls import path
from .views import add_to_cart, remove_from_cart

app_name = 'cartapp'

urlpatterns = [
    path('cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove/<slug>', remove_from_cart, name='remove_from_cart'),
]
