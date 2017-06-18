"""PublicationPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='homepage'),
    url(r'^registration/$', views.signup_user, name='signup_user'),
    url(r'^login/$', views.loginForm, name='login_user'),
    url(r'^userdashboard/$', views.dashboard_user, name='userdashboard'),
    url(r'^publisherdashboard/$', views.dashboard_publisher, name='publisherdashboard'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userdashboard/editprofile/$', views.edit_profile, name='edit_profile'),

    # url(r'^registration/regcheck/$', views.signup_user, name='signup_check'),
]
