from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from datetime import datetime
# Create your views here.

def delete(request, id):
    if request.user.is_authenticated():
        Task.objects.filter(user=request.user,id=id).delete()
        tasks = Task.objects.all().filter(user=request.user).order_by("done")
        context = {
            'tasks':tasks,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')

def done(request, id):
    if request.user.is_authenticated():
        task = Task.objects.filter(user=request.user,id=id)
        if task[0].done == False:
            task.update(done=True)
        else:
            task.update(done=False)
        tasks = Task.objects.all().filter(user=request.user).order_by("done")
        context = {
            'tasks':tasks,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')

def edit(request, id):
    if request.user.is_authenticated():
        task = Task.objects.filter(user=request.user,id=id)[0]
        if task.deadline == None:
            task.deadline = datetime.now
        form = TaskForm(request.POST or None, instance=task)
        context = {
    		"form": form
    	}
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        return render(request, 'edit.html', context)
    else:
        return redirect('/accounts/login')
