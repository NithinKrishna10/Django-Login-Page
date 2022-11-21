from django import views
from django.urls import include, path
from . import views


urlpatterns = [
    path('card',views.card_view,name="card"),
   
     
    
]