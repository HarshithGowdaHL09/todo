from django.urls import path
from . import views
urlpatterns = [
    #add rask
    path('addTask/', views.addTask, name='addTask'),

    #mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),

    #delete Task
    path('delete/<int:pk>', views.delete_task, name='delete_task'),

    #undo task or undone 
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    #edit task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task')
]
