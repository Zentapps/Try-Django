
from django.contrib import admin
from django.urls import include, path,re_path
from django.conf.urls.static import static
from django.conf import settings as SETTINGS

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('websites.urls')),
    re_path(r'^posts/', include('posts.urls',namespace='posts')),

    re_path(r'^api/v1/auth/', include('api.v1.authentication.urls', namespace="api_v1_authentication")),
    # re_path(r'^api/v1/posts/', include('api.v1.posts.urls', namespace="api_v1_posts")),

]

if SETTINGS.DEBUG: # URL pattern for serving files in debug mode
    urlpatterns += static(SETTINGS.STATIC_URL, document_root=SETTINGS.STATIC_ROOT)
    urlpatterns += static(SETTINGS.MEDIA_URL, document_root=SETTINGS.MEDIA_ROOT)
