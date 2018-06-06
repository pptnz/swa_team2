from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo, name='todo_add'),
    url(r'^post/$', views.post_todo, name='post_todo')
]