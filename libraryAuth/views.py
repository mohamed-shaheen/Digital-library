from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
# Create your views here.



def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)

    context = {'form':form}      

    return render(request,'signup.html', context)