from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_up_page, name='sign_up_page'),
    url(r'^activate_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_email, name='activate_email')
]
