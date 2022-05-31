from django.contrib import admin

# Register your models here.

from .models import Reddit

@admin.register(Reddit)
class RedditAdmin(admin.ModelAdmin):
    list_display = ("user_name", "title", "pub_date")

from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")