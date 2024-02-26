from django.urls import  re_path
from . import views


app_name = 'websites'


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^post/(?P<pk>.*)/$', views.post, name='post'),
    re_path(r'^profile/$', views.profile, name='profile'),

]