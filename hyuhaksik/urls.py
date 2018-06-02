from django.conf.urls import url, include
#from django.urls import path
from . import views

urlpatterns = [
    url(r'^keyboard/', views.keyboard),
    url(r'^message', views.answer),
]
