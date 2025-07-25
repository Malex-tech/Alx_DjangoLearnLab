"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from relationship_app import views
from relationship_app.views import add_book
from django.views import AddBookView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# relationship_app/urls.py
from django.urls import path
from relationship_app import views 
from django.contrib import admin

urlpatterns = [
    path('', views.library_home, name='library-home'),
    path('register/', views.register_view, name='register'),
    #path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('roles/', include('relationship_app.urls')),
    path('books/add/', AddBookView.as_view(), name='add_book'),
]
