from django.db import models




class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"
    