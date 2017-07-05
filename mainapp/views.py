from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify

from mainapp.forms import SignUpForm, LoginForm, SaveProfilePublisher, SaveProfileUser, SaveManuscriptDetails, \
    UpdateStatusManuscript
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


def user_home(request):
    try:
        user = UserSignup.objects.get(id=request.session['uid'])
        list_publishers = PublisherProfile.objects.all()
        return render(request, 'userhome.html', {'user': user, 'list_publishers': list_publishers})
    except:
        return HttpResponse("Page unable to access.")


def publisher_home(request):
    try:
        us = PubSignup.objects.get(id=request.session['uid'])
        usprofile = PublisherProfile.objects.get(user=us)
        manscpt = Manuscript.objects.filter(publisher=usprofile)
        return render(request, 'publisherhome.html', {'us': us, 'manscpt': manscpt})
    except:
        return HttpResponse("Page unable to access.")


def dashboard_user(request):
    try:
        us = UserSignup.objects.get(id=request.session['uid'])
        submissions = Manuscript.objects.filter(email=us.email)
        return render(request, 'userdashboard.html', {'us': us, 'submissions': submissions})
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
                    errorstring = "Wrong email or password."
                    return render(request, 'login.html', {'errorstring': errorstring})

            elif form.role == "Publisher":
                try:
                    user = PubSignup.objects.get(email=form.cleaned_data.get('loginemail'),
                                                 password=form.cleaned_data.get('loginpassword'))
                    request.session['uid'] = user.id
                    # return render(request, 'publisherdashboard.html', {'user': user})
                    return redirect('/publisherdashboard', user='user')
                    # dashboard_publisher(request, user)
                except PubSignup.DoesNotExist:
                    errorstring = "Wrong email or password."
                    return render(request, 'login.html', {'errorstring': errorstring})

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


def user_profile(request):
    op = UserSignup.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        success = False
        form = SaveProfileUser(request.POST, request.FILES)
        if form.is_valid():
            try:
                nuser = UserProfile.objects.get(user=op)
                nuser.photo = form.cleaned_data.get('profileimage')
                nuser.full_name = form.cleaned_data.get('full_name')
                nuser.birth_date = form.cleaned_data.get('birth_date')
                nuser.books_wrote = form.cleaned_data.get('books_wrote')
                nuser.journal_wrote = form.cleaned_data.get('journal_wrote')
                nuser.experience = form.cleaned_data.get('experience')
                nuser.address = form.cleaned_data.get('address')
                nuser.phoneno = form.cleaned_data.get('phoneno')
                nuser.save()
            except:
                return render(request, 'userprofile.html', {'success': success, 'op': op})
            # p.save()
            success = True
        return render(request, 'userprofile.html', {'success': success, 'op': op})
    return render(request, 'userprofile.html', {'op': op})


def publisher_profile(request):
    op = PubSignup.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        success = False
        form = SaveProfilePublisher(request.POST, request.FILES)
        if form.is_valid():
            try:
                nuser = PublisherProfile.objects.get(user=op)
                nuser.photo = form.cleaned_data.get('profileimage')
                nuser.full_name = form.cleaned_data.get('fullname')
                nuser.cmpny_name = form.cleaned_data.get('companyname')
                nuser.cmpny_website = form.cleaned_data.get('companywebsite')
                nuser.aboutcmpny = form.cleaned_data.get('aboutcmpny')
                nuser.cmpny_address = form.cleaned_data.get('address')
                nuser.phoneno = form.cleaned_data.get('phoneno')
                nuser.slug = slugify(nuser.cmpny_name)
                nuser.save()
            except:
                return render(request, 'publisher_profile.html', {'success': success, 'op': op})
            # p.save()
            success = True
        return render(request, 'publisher_profile.html', {'success': success, 'op': op})

    return render(request, 'publisher_profile.html', {'op': op})


def single_post(request, slug):
    obj = PublisherProfile.objects.get(slug=slug)
    userop = UserSignup.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        success = False
        form = SaveManuscriptDetails(request.POST, request.FILES)
        if form.is_valid():
            # try:
            nuser = Manuscript.objects.get(publisher=obj)
            nuser.title = form.cleaned_data.get('title')
            nuser.department = form.cleaned_data.get('department')
            nuser.name = form.cleaned_data.get('name')
            nuser.email = userop.email
            nuser.phone = form.cleaned_data.get('phone')
            nuser.mtitle = form.cleaned_data.get('mtitle')
            nuser.mabstract = form.cleaned_data.get('mabstract')
            nuser.mdocfile = form.cleaned_data.get('mdocfile')
            nuser.slug = slugify(nuser.title)
            nuser.save()
            success = True
            # except:
            #     return render(request, 'submitapplication.html', {'success': success})
            # p.save()
        return redirect('/userdashboard/')
    return render(request, 'submitapplication.html', {'userop': userop})


def checkApplication(request):
    # app = Manuscript.objects.get(title=title)
    return render(request, 'checkapplication.html')


def reviewapplication(request, slug):
    application = Manuscript.objects.get(slug=slug)
    if request.method == 'POST':
        success = False
        form = UpdateStatusManuscript(request.POST)
        if form.is_valid():
            try:
                application.status = form.cleaned_data.get('status')
                application.save()
                success = True
                return redirect('/publisherdashboard/home/')
            except:
                return HttpResponse("Page unable to access.")

    return render(request, 'checkapplication.html', {'application': application})
