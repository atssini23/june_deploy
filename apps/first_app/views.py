from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    all_users = User.objects.all()
    for user in all_users:
        print user.first_name, user.last_name, user.email, user.password
    return render(request, 'first_app/index.html')

def add_user(request):
    print request.POST
    results = User.objects.register_val(request.POST)
    if not results['valid']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User has been created. Please login')

        return redirect('/')

def login(request):
    results = User.objects.login_val(request.POST)
    if not results['valid']:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        messages.success(request, "You have successfully logged in!!!")
    return render(request, 'first_app/success.html')
