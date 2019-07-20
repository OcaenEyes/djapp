from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from .form import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def regist(request):
    return render(request,'regist.html')