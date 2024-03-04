from django.shortcuts import render
from django.views import generic,View
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import Digizilla

class DigizillaList(generic.ListView):
    model = Digizilla

class DigizillaDetail(generic.DetailView):
    model = Digizilla

class DigizillaCreate(generic.CreateView):
    model = Digizilla
    fields = '__all__'
    success_url = '/odoo/'

class DigizillaUpdate(generic.UpdateView):
    model = Digizilla
    fields = '__all__'
    success_url = '/odoo/'

class DigizillaPDFView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="digizilla_report.pdf"'

        p = canvas.Canvas(response)

        digizillas = Digizilla.objects.all()

        p.setFont("Helvetica", 12)

        for digizilla in digizillas:
            p.drawString(100, 700, f"Name: {digizilla.name}")
            p.drawString(100, 680, f"Gender: {digizilla.gender}")
            p.drawString(100, 660, f"Country: {digizilla.country}")
            p.drawString(100, 640, f"Joining Date: {digizilla.joining_date}")
            p.drawString(100, 620, f"Tags: {', '.join([tag.name for tag in digizilla.tags.all()])}")
            p.drawString(100, 600, f"Customers: {', '.join([customer.username for customer in digizilla.customers.all()])}")
            p.drawString(100, 580, f"Company: {digizilla.company.name}")
            p.drawString(100, 560, f"Notes: {digizilla.notes}")
            p.drawString(100, 540, f"Comments: {digizilla.comments}")

            p.showPage()

        p.save()

        return response