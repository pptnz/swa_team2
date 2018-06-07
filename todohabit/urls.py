"""todohabit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from signin.views import sign_in_redirect

urlpatterns = [
    url(r'^sign_in/', include('signin.urls')),
    url(r'^sign_up/', include('signup.urls')),
    url(r'^sign_out/', include('headerbar.urls')),
    url(r'^find_password/', include('findpassword.urls')),
    url(r'^change_password/', include('changepassword.urls')),
    url(r'^todo/', include('todo.urls')),
    url(r'^habitmaker/', include('habitmaker.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^.*$', sign_in_redirect)
]
