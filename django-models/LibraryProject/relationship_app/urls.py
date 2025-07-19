# relationship_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Book routes
    path('add_book/', views.add_book, name='add_book'),  # <-- THIS
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # <-- AND THIS
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]