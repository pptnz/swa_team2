from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.habit_list, name='habit_list'),
    url(r'^(?P<pk>\d+)/toggle_success/$', views.toggle_success, name='toggle_success')
]