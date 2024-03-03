from django.urls import path

from .views import DigizillaList,DigizillaCreate

#  odoo/
urlpatterns = [
    path('',DigizillaList.as_view()),
    path('add/',DigizillaCreate.as_view()),
]
