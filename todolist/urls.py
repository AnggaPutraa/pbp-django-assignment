from django.urls import path
from todolist.views import  regist_user, login_user, logout_user, show_todos, create_task, update_task, delete_task, create_task_with_ajax, get_todolist_as_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todos, name='show_todos'),
    path('create-task/', create_task,  name='create_task'),
    path('register/', regist_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-task/<str:key>/', update_task, name='update_task'),
    path('delete-task/<str:key>/', delete_task, name="delete_task"),
    path('json/', get_todolist_as_json, name='get_todolist_as_json'),
    path('add/', create_task_with_ajax, name='create_task_with_ajax'),
]
