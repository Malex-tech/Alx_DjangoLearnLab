from django.urls import path
from . import views
from blog import views
from .views import PostByTagListView
from .views import(
    PostListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

app_name = 'blog'

urlpatterns = [
    # Auth & Profile
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Class-based Post Views
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Function-based Post Views
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # Comments (CBV only for check compliance)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

urlpatterns = [
    path('', views.index, name='index'),
     path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
]
