from django.contrib import admin 
from django.urls import path
from . import views 

 
 
urlpatterns = [ 
    path('', views.home, name='home'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('contact', views.contact, name='contact'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),

] 
