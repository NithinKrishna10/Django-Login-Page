from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.login_view,name="login"),
    path('home',views.home_view,name="home"),
    path('signout',views.signout,name="signout"),
    
    
]