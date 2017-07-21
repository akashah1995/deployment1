from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [

    url(r'/new$', views.create),
    url(r'/add$', views.add),
    url(r'/home$', views.index),
    url(r'/addpage$', views.addpage),
    url(r'/back$', views.back),
    url(r'/(?P<variable>\d+)$', views.show),
    url(r'/(?P<variable>\d+)/edit$', views.edit),
    url(r'/update$', views.update),
    url(r'/(?P<variable>\d+)/delete$', views.delete),
]