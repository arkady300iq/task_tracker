from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("in_progress", "In progress"),
        ("done", "Done")
    ]
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]
    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=23, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=23, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
