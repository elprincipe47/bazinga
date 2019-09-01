from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path('webhook', views.webhook),
    path('', views.OrderList.as_view(), name='order_list'),
    path('<int:pk>', views.OrderDetail.as_view(), name='order_detail'),
    path('', views.OrderCreate.as_view(), name='order_create'),
    path('update/<int:pk>', views.OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>', views.OrderDelete.as_view(), name='order_delete'),

]
