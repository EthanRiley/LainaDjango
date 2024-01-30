from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Reservation, Blog

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

def login_page(request):
    return render(request, 'registration/login.html', name='login')

def profile_view(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(customer=request.user)
        return render(request, 'profile.html', {'reservations': reservations, 'user': request.user})
    else:
        return redirect('login')

def reservation_detail_view(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    blogs = Blog.objects.filter(reservation=reservation)
    return render(request, 'reservations/reservation_detail.html', 
                  {'reservation': reservation,
                   'blogs': blogs})

def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/blog_view.html', {'blog': blog})



