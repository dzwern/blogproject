from django.conf.urls import url

from . import views
app_name='comment'


urlpatterns=[
    url(r'^comment/post/(\d+)/$',views.post_comment,name='post_comment'),
]

