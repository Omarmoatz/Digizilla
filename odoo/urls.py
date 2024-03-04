from django.urls import path

from .views import DigizillaList,DigizillaDetail,DigizillaCreate,DigizillaUpdate,DigizillaPDFView

app_name = 'odoo'

#  odoo/
urlpatterns = [
    path('',DigizillaList.as_view(),name='list'),
    path('<int:pk>/',DigizillaDetail.as_view(),name='detail'),
    path('add/',DigizillaCreate.as_view(),name='add'),
    path('<int:pk>/update/',DigizillaUpdate.as_view(),name='update'),
    path('digizilla/pdf/', DigizillaPDFView.as_view(), name='digizilla_pdf'),
]
