# relationship_app/views.py

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Yo Alex! Welcome to the Home View 😎")


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
