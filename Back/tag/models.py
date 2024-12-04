from django.db import models
from users.models import CustomUser

# This is a test for GitHub

class Tag(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='no_name')
    created = models.DateTimeField()
    memo = models.TextField(max_length=200)


    def __str__(self) -> str:
        return f"{self.name} - {self.user.username}"
    