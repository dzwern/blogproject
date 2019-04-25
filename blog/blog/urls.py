from django.conf.urls import url
from . import views

app_name='blog'

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.single,name='single'),
    url(r'^date/(.*?)/$',views.archives,name='archives'),
    url(r'^class/(\d+)/$',views.classies,name='classies'),
    url(r'^tags/(\d+)/$',views.tags,name='tags'),



]