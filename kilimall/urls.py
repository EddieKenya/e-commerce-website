from django.urls import path
from.import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.store, name='store'),
    path('update_item/', views.updateItem, name='update_item'),
]