from django.urls import path

from .views import DigizillaList,DigizillaDetail,DigizillaCreate,DigizillaUpdate

#  odoo/
urlpatterns = [
    path('',DigizillaList.as_view()),
    path('<int:pk>/',DigizillaDetail.as_view()),
    path('add/',DigizillaCreate.as_view()),
    path('<int:pk>/update/',DigizillaUpdate.as_view()),
]
