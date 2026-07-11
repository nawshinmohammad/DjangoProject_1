from django.shortcuts import render, redirect,get_object_or_404
from .models import Tasks
from .forms import TaskForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render(request, 'tasks/homepage.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def task_list(request):
    task = Tasks.objects.filter(owner=request.user)
    
    search = request.GET.get("search")
    if search:
        task = task.filter(Q(task_title__icontains=search)|
                           Q(description__icontains=search))
 
    return render(request, 'tasks/task_list.html', {'task' : task, 'search':search,})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form,})

@login_required
def task_details(request, id):

    task = get_object_or_404(Tasks, id=id,  owner=request.user)

    return render(request, 'tasks/task_detail.html', {'task': task})


def update_task(request, id):
    task = get_object_or_404(Tasks,id=id,owner=request.user)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("task_list")

    return render(request, "tasks/task_form.html", {"form": form})


def delete_task(request, id):
    task = get_object_or_404(Tasks,id=id,owner=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})

