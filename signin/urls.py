from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_in_page, name='sign_in_page')
]