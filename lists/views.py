from django.http import HttpResponse
from django.shortcuts import render
from lists import templates

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')