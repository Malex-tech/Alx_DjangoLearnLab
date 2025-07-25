# relationship_app/urls.py
from django.urls import path  # This line was missing!
from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views


urlpatterns = [
   # path('', views.home_view, name='home'),  # 👈 now root works
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', 
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('list-books/', views.list_books, name='list_books'),  # Make sure this exists
    path('', views.home, name='home'),  # Home page
    path('login/', include('relationship_app.urls')),  # this includes the broken stuff
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.library_home, name='library-home'),  # <-- 🔥 THIS is the line throwing errors
]
