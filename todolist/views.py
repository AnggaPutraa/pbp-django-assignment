import datetime
from tkinter import NO
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from todolist.models import TaskItem

def regist_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        is_user_already_exist = User.objects.filter(username=username).exists()
        if password_1 == password_2 and not is_user_already_exist:
            user = User.objects.create_user(
                username=username,
                password=password_2
            )
            if user is not None:
                user.save()
                return redirect('todolist:login')
            else:
                messages.info(
                    request,
                    'Ops! something went wrong'
                )
        elif password_1 != password_2:
            messages.info(
                request,
                'Passowrd doesnt match'
            )
        elif is_user_already_exist:
            messages.info(
                request,
                'User already exist'
            )
        else:
            messages.info(
                request,
                'Ops! something went wrong'
            )

    return render(
        request,
        'regist.html',
        {}
    )

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse('todolist:show_todos')
            )
            response.set_cookie(
                'username',
                username
            )
            response.set_cookie(
                'last_login',
                str(datetime.datetime.now())
            )
            return response
        else:
            messages.info(
                request,
                'Username atau password salah!'
            )

    return render(
        request,
        'login.html',
        {}
    )

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(
        reverse('todolist:login')
    )
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todos(request):
    data = TaskItem.objects.filter(
        user = request.user
    )
    return render(
        request,
        'todolist.html',
        {
            'username': request.COOKIES['username'],
            'last_login': request.COOKIES['last_login'],
            'todos': data,
        }
    )

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        TaskItem.objects.create(
            user=user, 
            title=title, 
            description=description
        )
        return redirect('todolist:show_todos')
    
    return render(
        request,
        'create_task.html',
        {}
    )

@login_required(login_url='/todolist/login/')
def update_task(request, key):
    task = TaskItem.objects.get(
        user = request.user,
        pk = key
    )
    task.is_finished = not task.is_finished
    task.save()
    return redirect(
        'todolist:show_todos'
    )

@login_required(login_url='/todolist/login/')
def delete_task(request, key):
    task = TaskItem.objects.get(
        user = request.user,
        pk = key
    )
    task.delete()

    return redirect(
        'todolist:show_todos'
    )
