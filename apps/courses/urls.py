from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [

    url(r'/$', views.index),
    url(r'/addcourse$', views.addcourse),
    url(r'/destroy/(?P<variable>\d+)$', views.deletepage),
    url(r'/remove/(?P<variable>\d+)$', views.remove),
    url(r'/back$', views.back)
]