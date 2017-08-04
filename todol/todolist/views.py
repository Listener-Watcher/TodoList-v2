from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import TaskSerializer
# Create your views here.
INCREASE = ''
DECREASE = '-'
sort_by = {'priority':INCREASE, 'deadline':DECREASE}

def about(request):
    return render(request, 'about.html',{})

def index(request):
    if request.user.is_authenticated():
        tasks = Task.objects.all().filter(user=request.user).order_by("created_at","done")
        context = {
            'tasks':tasks,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('/accounts/login')

def details(request, id):
    if request.user.is_authenticated():
        task = Task.objects.get(id=id)
        context = {
            'task':task,
        }
        return render(request, 'details.html', context)
    else:
        return redirect('/accounts/login')

def add(request):
    if request.user.is_authenticated():

        form = TaskForm(request.POST or None)
        context = {
    		"form": form
    	}
        if form.is_valid():
            # form.data.update(user=request.user)
            form.save()
            task = Task.objects.filter(title=form.data['title'])
            task.update(user=request.user)
            print form.data
            return redirect('/dashboard')
    		# instance = form.save(commit=False)
    		# # if not instance.full_name:
    		# # 	instance.full_name = "Justin"
    		# instance.save()
        return render(request, 'add.html', context)
    else:
        return redirect('/accounts/login')

def dashboard(request):
    global sort_by, INCREASE, DECREASE
    if request.user.is_authenticated():
        KEY = ''
        if request.method == "POST":
            KEY = request.POST.get("priority")
            if KEY is None:
                KEY = request.POST.get("deadline")
            if KEY == 'priority' or KEY == 'deadline':
                if sort_by[KEY] == INCREASE:
                    sort_by[KEY] = DECREASE
                else:
                    sort_by[KEY] = INCREASE
            else:
                KEY = ''
        if KEY != '':
            print sort_by[KEY] + KEY
            tasks = Task.objects.all().filter(user=request.user).order_by("done", sort_by[KEY] + KEY)
        else:
            tasks = Task.objects.all().filter(user=request.user).order_by("created_at","done")
        context = {
            'tasks':tasks,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')


class TaskList(generics.ListCreateAPIView):
    def get(self, request, format=None):
        task = Task.objects.all().order_by('-created_at')
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    @permission_classes((IsAdminUser, ))
    def Task(self, request, format=None):
        user = request.user
        serializer = TaskSerializer(data=request.data, context={'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_REQUEST)
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
