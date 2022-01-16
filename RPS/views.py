from django.shortcuts import render
from django.views.generic import CreateView

def home_page(request):
     return render(request,'index.html')

def help_page(request):
     return render(request,'help.html')
