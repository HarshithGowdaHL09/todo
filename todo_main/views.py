from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks1 = Task.objects.filter(is_completed=False)
    completed = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks1,
        'completed':completed
    }
    
    return render(request, 'home.html', context)