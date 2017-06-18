from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from mainapp.forms import SignUpForm, LoginForm
from .models import *


def home_page(request):
    return render(request, 'home.html')


def signup_user(request):
    if request.method == 'POST':
        success = False
        form = SignUpForm(request.POST)
        form.role = str(request.POST.get('role'))
        if form.is_valid():
            if form.role == "Author":
                p = UserSignup(
                    name=form.cleaned_data.get('name'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password')
                )
                p.save()
                success = True
            elif form.role == "Publisher":
                p = PubSignup(
                    name=form.cleaned_data.get('name'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password')
                )
                p.save()
                success = True
            return render(request, 'regcheck.html', {'success': success})

    return render(request, 'registration.html')


def dashboard_user(request):
    try:
        user = UserSignup.objects.get(id=request.session['uid'])
        return render(request, 'userdashboard.html', {'user': user})
    except:
        return HttpResponse("Page unable to access.")


def dashboard_publisher(request):
    try:
        user = PubSignup.objects.get(id=request.session['uid'])
        return render(request, 'publisherdashboard.html', {'user': user})
    except:
        return HttpResponse("Page unable to access.")


def loginForm(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.role = str(request.POST.get('role'))
        if form.is_valid():
            if form.role == "Author":
                try:
                    user = UserSignup.objects.get(email=form.cleaned_data.get('loginemail'),
                                                  password=form.cleaned_data.get('loginpassword'))
                    request.session['uid'] = user.id
                    # curuser = UserSignup.objects.filter(email=user.email)
                    # return render(request, 'userdashboard.html', {'user': user})
                    return redirect('/userdashboard', user='user')
                    # dashboard_user(request, user)
                except UserSignup.DoesNotExist:
                    return HttpResponse("Wrong Username Password")

            elif form.role == "Publisher":
                try:
                    user = PubSignup.objects.get(email=form.cleaned_data.get('loginemail'),
                                                 password=form.cleaned_data.get('loginpassword'))
                    request.session['uid'] = user.id
                    # return render(request, 'publisherdashboard.html', {'user': user})
                    return redirect('/publisherdashboard')
                    # dashboard_publisher(request, user)
                except PubSignup.DoesNotExist:
                    return HttpResponse("Wrong Username Password")

            else:
                return HttpResponse("Something wrong go back and login again.")
        else:
            return HttpResponse("Something wrong go back and login again.")

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['uid']
        return redirect('/')
    except:
        pass
    return redirect('/')


def edit_profile(request):
    return redirect('/')




