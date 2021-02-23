from django.shortcuts import render
from .models import About
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def courses(request):
    return render(request,'pages/courses.html')

def c(request):
    return render(request,'pages/c.html')

def python(request):
    return render(request,'pages/python.html')
def java(request):
    return render(request,'pages/java.html')

class AboutCreateView(SuccessMessageMixin,CreateView):
    model = About
    template_name = 'pages/about.html'
    fields = ['name','email','query']
    success_message = "Mail Sent successfully!, We will contact you soon"
