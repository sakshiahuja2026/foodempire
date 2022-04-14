from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import food
from django.views.generic import ListView,DetailView

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