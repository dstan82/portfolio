from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Create a blog models
# title
# pub_dat
# body
# image

# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin
