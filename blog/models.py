from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    Content = models.TextField()
    writer = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    age = models.CharField(max_length=2, default=0)
    

    def __str__(self):
        return self.title

# Create your models here.