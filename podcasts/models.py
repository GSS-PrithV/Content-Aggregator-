from statistics import mode
from turtle import title
from django.db import models

# As a user I would like to:
# - Know the title the post
# - Know the description of the post
# - Know when the post was published
# - Have a clickable URL so I can listen to the episode
# - See any image from the post so I can scroll to look
# - See the name of the user who posted it
# 
# As a developer, I would like to:
# - Have a uniquely identifiable attribute for each episode so I can avoid duplicating episodes in the database.

class Reddit(models.Model):
    title = models.CharField(max_length= 1000)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    thumbnail = models.URLField()
    user_name = models.CharField(max_length= 200)
    guid = models.CharField(max_length= 50)

    def __str__(self) -> str:
        return f"{self.user_name}: {self.title}"

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"