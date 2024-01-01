from django.urls import path, include, re_path
from . import views
 
urlpatterns = [
  path('hello',views.say_hello),
  path('home', views.load_homepage),
  path('reservations', views.load_boarding_form),
  path('accounts/', include('django.contrib.auth.urls')),
 ]