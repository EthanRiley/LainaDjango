from django.urls import path
from . import views
 
urlpatterns = [
  path('hello',views.say_hello),
  path('home', views.load_homepage),
  path('reservations', views.load_boarding_form)
 ]