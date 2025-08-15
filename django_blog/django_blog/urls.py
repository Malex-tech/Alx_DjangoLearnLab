
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),  # Single include with namespace
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


