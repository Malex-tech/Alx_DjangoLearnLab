# relationship_app/urls.py
from django.urls import path  # This line was missing!
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),  # 👈 now root works
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', 
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('list-books/', views.list_books, name='list_books'),  # Make sure this exists
]
