from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_add, name='todo_add')
]