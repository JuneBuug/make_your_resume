# resume_prac/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.resume_list, name='list'),
    url(r'^write$', views.resume_write, name='write'),
    url(r'^(?P<resume_id>\d+)$',views.resume_detail,name="detail"),
    url(r'^search/$',views.resume_search,name="search"),
]
