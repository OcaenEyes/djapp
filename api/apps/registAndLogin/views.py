from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from .form import *

# Create your views here.

def index(request):
    user = request.session.get('user',False)

    return render(request,'index.tml')


def registAndLogin(request):
    user = request.session.get('user',False)
    print(user)
    if not user:
        return render(request,'login.html')
    else:
        return HttpResponseRedirect('/index/')


def regist(request):
    check =False
    if request.method == 'POST':
        form =