from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from task_tracker import models
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from task_tracker.mixins import UserIsOwnerMixin
from task_tracker.forms import TaskForm, TaskFilterForm
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "task_tracker/task_list.html"
    login_url = 'task_tracker/login.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "task_tracker/task_detail.html"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = "task_tracker/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task_tracker:task-list")

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskCompleteView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect(reverse_lazy("task_tracker:task-list"))
    
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)
    

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    template_name = "task_tracker/task_update_form.html"
    success_url = reverse_lazy("task_tracker:task-list")

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy("task_tracker:task-list")
    template_name = "task_tracker/task_delete_confirmation.html"


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_tracker:task-list')  # Убедитесь, что это правильно
    else:
        form = UserCreationForm()
    return render(request, 'task_tracker/register.html', {'form': form})