from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.habit_list, name='habit_list')
]