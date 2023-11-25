from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title