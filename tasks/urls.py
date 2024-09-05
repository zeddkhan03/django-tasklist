from django.urls import path
from . import views

# URL patterns for the task management app
urlpatterns = [
    
    # URL for the task list page. Maps to the 'task_list' view function.
    path('', views.task_list, name='task_list'),
    
    # URL for deleting a specific task. Captures the task_id from the URL and maps to the 'delete_task' view function.
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # URL for editing a specific task. Captures the task_id from the URL and maps to the 'edit_task' view function.
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]
