from django.shortcuts import render
from .models import DestinatarioEncomienda
# Create your views here.
def home(request):
    productos = DestinatarioEncomienda.objects.all()
    data = {
         'productos': productos
    }
    return render(request,'app/home.html', data)