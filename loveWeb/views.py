from django.shortcuts import render, redirect, get_object_or_404
from user.forms import *
def home(request):
    context = {}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return render(request, 'index.html', context)
    else:
        login_form = LoginForm()
    context['login_form'] = login_form
    return render(request, 'index.html', context)

def time(request):
    context = {}
    return render(request, 'time.html', context)

def hongbao(request):
    context = {}
    return render(request, 'hongbao.html', context)