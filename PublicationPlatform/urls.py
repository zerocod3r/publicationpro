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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from mainapp import views
from PublicationPlatform import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='homepage'),
    url(r'^registration/$', views.signup_user, name='signup_user'),
    url(r'^login/$', views.loginForm, name='login_user'),
    url(r'^userdashboard/$', views.dashboard_user, name='userdashboard'),
    url(r'^publisherdashboard/$', views.dashboard_publisher, name='publisherdashboard'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userdashboard/editprofile/$', views.user_profile, name='user_profile'),
    url(r'^publisherdashboard/editprofile/$', views.publisher_profile, name='publisher_profile'),
    url(r'^userdashboard/home/$', views.user_home, name='user_home'),
    url(r'^publisherdashboard/home/$', views.publisher_home, name='publisher_home'),
    url(r'^userdashboard/checkapplication/$', views.checkApplication, name='checkapplication'),
    url(r'^userdashboard/home/submit/(?P<slug>[-\w]+)/$', views.single_post, name='single_post'),
    url(r'^publisherdashboard/home/review/(?P<slug>[-\w]+)/$', views.reviewapplication, name='reviewapplication')

    # url(r'^registration/regcheck/$', views.signup_user, name='signup_check'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
