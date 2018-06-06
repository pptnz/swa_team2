from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo, name='todo_add'),
    url(r'^new/$', views.add_new, name='add_new')
]