from django.shortcuts import render
from .models import Todo
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        Todo.objects.create(title=title, category=category, description=description)
        return redirect('list')
    return render(request, 'create.html')

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.category = request.POST['category']
        todo.description = request.POST['description']
        todo.save()
        return redirect('list')
    return render(request, 'update.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')
    return render(request, 'delete.html', {'todo': todo})
