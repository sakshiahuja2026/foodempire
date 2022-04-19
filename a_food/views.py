from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from UserApp.models import cart
from .models import food
from django.views.generic import ListView,DetailView
from .models import *
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models

from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from UserApp.models import User

# Create your views here.
class createfood(CreateView):
    model = food
    fields='__all__'
    template_name='a_food/create.html'
    success_url='/a_food/view/'

def index(request):
    return render(request,"index.html")

class viewfood(ListView):
    model = food
    foods = food.objects.all()
    context_object_name = 'foods'
    template_name = "a_food/menu.html"
    
class detailfood(DetailView):
    model = food
    template_name = "user/template/detail.html"
class deletefood(DeleteView):
    model = food
    fields = '__all__'
    template_name = 'user/template/delete.html'
    success_url='/user/view/'
class updatefood(UpdateView):
    model = food
    fields = '__all__'
    template_name = 'user/template/update.html'
    success_url='/user/view/'

class CartListView(ListView):

    model = cart
    template_name = 'UserApp/cart.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_total"] = cart(user = self.request.user)
        return context

    def get_queryset(self):
        user = User.objects.filter(username = self.request.user).first()
        print("user", user)
        queryset = cart.objects.filter(Q(user__username = user))
        return queryset
    

class AddToCartView(LoginRequiredMixin, View):

    print("called")
    def post(self, request, *args, **kwargs):

        print("request", request.POST)
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')
        quan = int(request.POST.get('quantity', 1))
        # print("quan", quan)
        try:
            fid = food.objects.get(id = item_id)
        except Exception as e:
            fid= None

        user = User.objects.filter(username = request.user).first()
        # print("user", user)

        cart_item, created = cart.objects.get_or_create(user = user, fid = fid)
        print("CART_ITEM------->>>>", cart_item)
      
        cart_total = cart_item.get_cart_total
        get_cart_total = cart_item.get_total
        # print("Before cart_item_Total price", cart_item.quantity)

        if action == "add":
            if quan > 1:
                cart_item.quantity = cart_item.quantity + quan
                cart_total = cart_item.get_cart_total
            else:
                cart_item.quantity += 1
                cart_total = cart_item.get_cart_total

            cart_item.save()
        
        elif action == "remove":
            if cart_item.quantity <= 1:
                print("cart_item", cart_item)
                cart_item.delete()
                return JsonResponse({"product_total" : cart_total, "item_id":item_id, "get_cart_total" : get_cart_total}) 
            else:
                cart_item.quantity -= 1
                cart_total = cart_item.get_cart_total
                cart_item.save()

        elif action == "delete":
            cart_item.delete()
            return JsonResponse({"product_total" : cart_total, "item_id":item_id, "get_cart_total" : get_cart_total}) 

        # print("After cart item quan", cart_item.quantity)
        get_cart_total = cart_item.get_total
        cart_item.save()
        print("cart_item", cart_item)
        return JsonResponse({"product_total" : cart_total, "item_id":item_id, "get_cart_total" : get_cart_total}) 
