from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Ethan'})

def load_homepage(request):
    return render(request, 'home.html')

def load_boarding_form(request):
    return render(request, 'boarding_form.html')