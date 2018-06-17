

# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from.forms import FormName
def prof(request):
    return render(request,'user_profile/base.html')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('u:cp')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_profile/passreset.html', {
        'form': form,
    })
def resume(request):
    if request.method=='POST':
        form=FormName(data=request.POST)
        if form.is_valid():
            f=form.save()
            return HttpResponse("Done")
    else:
        form=FormName()
    return render(request,'user_profile/user.html',{'form':form})
