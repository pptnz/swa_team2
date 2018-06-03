from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_up_page, name='sign_up_page')
]
