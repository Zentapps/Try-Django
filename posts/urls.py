from django.urls import  re_path
from . import views


app_name = 'posts'


urlpatterns = [

    re_path(r'^create-post/$', views.create_post, name='create_post'),
    # re_path(r'^detail-post/(?P<pk>.*)/$', views.detail_post, name='detail_post'),
    re_path(r'^list-post/$', views.list_post, name='list_post'),
    re_path(r'^edit-post/(?P<pk>.*)/$', views.edit_post, name='edit_post'),

]