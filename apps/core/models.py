from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class Application(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project_name} - {self.user}'

