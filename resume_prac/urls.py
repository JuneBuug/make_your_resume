# resume_prac/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.resume_list, name='list'),
    url(r'^write$', views.resume_write, name='write'),
    url(r'^write2/(?P<resume_id>\d+)$', views.resume_write_2, name='write2'),
    url(r'^write3/(?P<resume_id>\d+)$', views.resume_write_3, name='write3'),
    url(r'^(?P<resume_id>\d+)$',views.resume_detail,name="detail"),
    url(r'^search/$',views.resume_search,name="search"),
    url(r'^(?P<resume_id>\d+)/add$',views.detail_add,name="detail_add"),
    url(r'^example/(?P<example_id>\d+)$',views.resume_templates,name="example"),
]
