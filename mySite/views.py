from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Reservation

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Ethan'})

def load_homepage(request):
    return render(request, 'home.html')

def load_boarding_form(request):
    return render(request, 'boarding_form.html')

def base_generic(request):
    return render(request, 'base_generic.html')

def reservation_list_view(request):
    queryset = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': queryset})


