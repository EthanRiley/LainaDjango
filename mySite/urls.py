from django.urls import path, include, re_path
from . import views
from django.contrib.auth.views import LoginView
 
urlpatterns = [
  path('hello',views.say_hello),
  path('home', views.load_homepage),
  path('reservations', views.load_boarding_form),
  path('accounts/', include('django.contrib.auth.urls')),
  path('base_generic', views.base_generic),
  path('reservation', views.reservation_list_view),
  path('login/', LoginView.as_view(template_name='reservations/login.html'), name='login'),
  path('accounts/profile/', views.profile_view, name='profile')
 ]