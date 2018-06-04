from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.find_password_page, name='find_password_page')
]