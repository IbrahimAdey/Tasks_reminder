from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('add-ajax/', views.task_list_ajax, name='task_add_ajax'),
    path('tasks-json/', views.task_list_ajax, name='task_list_ajax'),
    path('', views.home, name='home')
]