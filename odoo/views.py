from django.shortcuts import render
from django.views import generic
from .models import Digizilla

class DigizillaList(generic.ListView):
    model = Digizilla


