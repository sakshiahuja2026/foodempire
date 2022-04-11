from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import food
from django.views.generic import ListView

# Create your views here.
class createfood(CreateView):
    model = food
    fields='__all__'
    template_name='a_food/create.html'
    success_url='/a_food/view/'

def index(request):
    return render(request,"index.html")

class listfood(ListView):
    model = food
    foods = model.objects.all()
    context_object_name = 'foods'
    template_name = "a_food/menu.html"
