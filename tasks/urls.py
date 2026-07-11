from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('signup/', views.signup, name='signup'),
    path('task_list/',views.task_list, name= 'task_list'),
    path('task_create/', views.task_create, name='task_create'),
    path('taskdetails/<int:id>/', views.task_details, name='task_details'),
    path('update_task/<int:id>/', views.update_task, name='update_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
]