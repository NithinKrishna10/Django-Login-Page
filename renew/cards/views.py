from django.shortcuts import render

from . models import Bikes

# Create your views here.

def card_view(request):
    
    dict_dept = {
        
        'bike' : Bikes.objects.all()
    }
    
    return render(request,'cards.html',dict_dept)