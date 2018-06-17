from django.shortcuts import render
import requests
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import signup,regform,loginformm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Apptwo:index'))

def index(request):
    return render(request,'main.html')
def entry(request):

    if request.method=='POST':
        user_form=signup(data=request.POST)
        profile_form=regform(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            return HttpResponseRedirect(reverse('Apptwo:f'))
        else:
            print(user_form.errors,profile_form.errors)
            print("errror")
    else:
        user_form=signup()
        profile_form=regform()

    return render(request,'App_two/registerform.html',{'user_form':user_form,
            'profile_form':profile_form})
def loginpage(request):

    if request.method=='POST':
        form=loginformm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if(user):
                login(request,user)
                print("DONE")
                return HttpResponseRedirect(reverse('Apptwo:index'))
            else:
                print("Wornf password /username")
    else:
        form=loginformm()
    return render(request,'App_two/log.html',{'f':form})
def main(request):
    return render(request,'Apptwo/main.html')
