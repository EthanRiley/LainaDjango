from django.urls import path, include, re_path
from . import views
 
urlpatterns = [
  path('hello',
       views.say_hello),
  path('home', 
       views.load_homepage),
  path('reservations', 
       views.load_boarding_form),
  path('base_generic', 
       views.base_generic),
  path('reservation', 
       views.reservation_list_view),
  path('accounts/profile/',
        views.profile_view,
          name='profile'),
  path('reservation/<int:reservation_id>', views.reservation_detail_view, name='reservation_detail'),
 ]