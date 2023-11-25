from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("task/", views.TaskListCreateView.as_view(), name="task-list-create"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task-retrieve-destroy-update")
]
