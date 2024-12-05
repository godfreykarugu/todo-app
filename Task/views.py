from django.shortcuts import render, redirect

from .models import Task
from . form import TaskForm

# Create your views here.

def home(request):
    tasks = Task.objects.all().order_by('date_due')
    return render(request,'index.html',{'tasks':tasks})


def todo(request):
    tasks = Task.objects.filter(completed = False).order_by('date_due')
    return render(request,'todo.html',{'tasks':tasks})

def complete(request):
    tasks = Task.objects.filter(completed = True).order_by('date_due')
    return render(request,'complete.html',{'tasks':tasks})

def add(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
        

    return render(request,'add.html',{'form':form})

def details(request,pk):
    task = Task.objects.get(id=pk)
    return render(request,'details.html',{'task':task})

def delete(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render (request, 'update.html',{'form':form})

def add2(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        completed = False
        if title != "" and due_date != "":
            task = Task(
                title = title,
                description =description,
                date_due = due_date,
                completed = completed,
            )

            task.save()

            return redirect('home')
        else:
            return render(request,'add2.html',{})
    return render (request,'add2.html',{})

def update2(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        completed = 'completed' in request.POST
        
        if title != "" and due_date != "":
            
            task.title = title
            task.description =description
            task.date_due = due_date
            task.completed = completed
            
            

            task.save()

            return redirect('home')
        else:
            return render(request,'update2.html',{'task':task})
    return render (request,'update2.html',{'task':task})

def search(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    if query:
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
    else:
        tasks = Task.objects.all()  # If no query, show all tasks

    return render(request, 'search.html', {'tasks': tasks, 'query': query})


def toggle_complete(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')
