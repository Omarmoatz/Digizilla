from django.shortcuts import render
from django.views import generic
from .models import Digizilla

class DigizillaList(generic.ListView):
    model = Digizilla

class DigizillaDetail(generic.DetailView):
    model = Digizilla

class DigizillaCreate(generic.CreateView):
    model = Digizilla
    fields = '__all__'
    success_url = '/odoo/'

class DigizillaCreate(generic.UpdateView):
    model = Digizilla
    fields = '__all__'
    success_url = '/odoo/'