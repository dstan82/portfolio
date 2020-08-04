from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=50, default='Please add a title')

    def __str__(self):
        return self.title
