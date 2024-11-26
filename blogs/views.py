from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def register(request):
    return render(request,"Register.html")

def Login(request):
    return render(request,"login_sol.html")

def All(request):
    return render(request,"all_Pro.html")

def apply(request):
    return render(request,"apply_work.html")

def add(request):
    return render(request,"Add_pro.html")

def progress(request):
    return render(request,"pro_progress.html")