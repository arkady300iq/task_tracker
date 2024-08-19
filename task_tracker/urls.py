from django.urls import path
from django.contrib.auth import views as auth_views
from task_tracker import views
from task_tracker.views import CommentDeleteView, CommentUpdateView


app_name = "task_tracker"

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/complete/', views.TaskCompleteView.as_view(), name='task-complete'),
    path('login/', auth_views.LoginView.as_view(template_name='task_tracker/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


]



