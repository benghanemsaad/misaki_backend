from django.urls import path
from . import products, order, clients

urlpatterns = [
    path('products/', products.getAllProducts),
    path('products/add/', products.addProduct),

    path('orders/', order.getAllOrders),
    path('orders/add/', order.addOrder),

    path('clients/', clients.getAllClients),
    path('clients/add/', clients.addClient),
]