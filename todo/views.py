from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def todo_list(request):
	todos = Todo.objects.all()
	return render(request,'Main/index.html',{'todo':todos})



def create_todo(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		Todo.objects.create(title=title,description=description)
	return redirect('/')


def complete_todo(request,todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.completed = True
	todo.save()
	return redirect('/')



def delete_todo(request,todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.delete()
	return redirect('/')