from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms and models
from App_Login.models import Profile
from App_Login.forms import ProfileForm, SignupForm
# message
from django.contrib import messages

def sign_up(request,*args,**kwargs):
    form = SignupForm()
    if request.method == 'P0ST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Create Account Successfully')
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request, 'App_Login/signup.html',context={'form':form})

def login_user(request, *args, **kwargs):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request, 'App_Login/login.html', context={'form':form})

@login_required
def logout_user(request, *args, **kwargs):
    logout(request)
    messages.warning(request, 'YOU ARE LOGGED OUT')
    return HttpResponseRedirect(reverse('App_Shop:home'))
@login_required
def user_profile(request, *args, **kwargs):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changed Save')
            form = ProfileForm(instance=profile)
    return render(request, 'App_Login/change_profile.html', context={'form':form})
