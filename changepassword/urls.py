from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.change_password_page, name='change_password_page')
]