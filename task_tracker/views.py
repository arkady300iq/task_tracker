from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from task_tracker import models
from django.views.generic import ListView, DetailView, CreateView
from task_tracker.forms import TaskForm

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "task_tracker/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "task_tracker/task_detail.html"

class TaskCreateView(CreateView):
    model = models.Task
    template_name = "task_tracker/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task_tracker:task-list")
