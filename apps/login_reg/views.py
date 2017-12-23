# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Users, Poke
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_reg/index.html')

def register(request):
    result = Users.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = Users.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['alias'] = result.alias
    try:
        request.session['recently_poked']
    except KeyError:
        request.session['recently_poked'] = 0
    context = {
        'users' : Users.objects.all()
    }
    return render(request, 'login_reg/pokes.html', context)

def logout(request):
    del request.session['user_id']
    return redirect('/')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_reg/success.html', context)
def pokes(request):
    context = {
        'users' : Users.objects.all(),
        'get_poked_count' : Poke.objects.get().count()

    }
    return render(request, 'login_reg/pokes.html', context)
def poke(request, id):
    poker = Users.objects.get(id=request.session['user_id'])
    poked = Users.objects.get(id=id)
    Poke.objects.create(poker=poker, poked=poked)
