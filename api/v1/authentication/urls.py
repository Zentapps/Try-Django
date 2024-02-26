from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

users_router = DefaultRouter()
users_router.register('posts', views.PostViewset, basename='posts')

app_name = 'api_v1_authentication'

urlpatterns = [

    re_path(r'^token/$', views.UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^login/$', views.Login.as_view()),
    re_path(r'^register/$', views.RegisterView.as_view()),
    re_path(r'^', include(users_router.urls)),

]
