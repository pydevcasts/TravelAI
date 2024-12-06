from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=50, null=True, blank=True)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.BooleanField()
    delayTime = models.DateTimeField()

    def __str__(self):
        return self.title
    


