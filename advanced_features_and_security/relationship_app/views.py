# relationship_app/views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Or wherever you want to send them after logout

def register_view(request):
    return render(request, 'relationship_app/register.html')  # or whatever template you have

def list_books(request):
    return render(request, 'relationship_app/book_list.html')  # or your actual template

def home(request):
    return render(request, 'home.html')

def home_view(request):
    return HttpResponse("Yo Alex! Welcome to the Home View 😎")

def library_home(request):
    return render(request, 'relationship_app/home.html')  # or any template you want

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Or wherever you want to send them
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
