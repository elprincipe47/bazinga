from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from orders.models import Order
from orders.utils import clean_payload
from django.shortcuts import redirect

import json
from django.urls import reverse_lazy, reverse

# Create your views here.

@csrf_exempt
def webhook(request):
    # build request object
    body_unicode = json.loads(request.body.decode('utf-8'))
    clean_pyld = clean_payload(body_unicode)
    order = Order.objects.create(**clean_pyld)
    return redirect('order_list')


class OrderList(ListView):
    model = Order


class OrderDetail(DetailView):
    model = Order
    fields = '__all__'


class OrderCreate(CreateView):
    model = Order


class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('order_list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
