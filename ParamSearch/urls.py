from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^health$', views.health, name='health'),
    url(r'^$', views.index, name='index'),
]
