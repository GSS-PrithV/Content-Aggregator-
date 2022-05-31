from urllib import response
from django.test import TestCase
from django.utils import timezone
from .models import Reddit
from django.urls.base import reverse
import feedparser


# Create your tests here.

class RedditTest(TestCase):
    def setUp(self):
        self.episode = Reddit.objects.create(
            title="My Awesome Podcast Episode",
            description="Look mom, I made it!",
            pub_date=timezone.now(),
            link="https://www.reddit.com/r/wallstreetbets/comments/uzncgy/most_anticipated_earnings_releases_for_the_week/",
            thumbnail="https://i.redd.it/qvqlxbsux7291.png",
            user_name="Reddit post",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it!")
        self.assertEqual(self.episode.link, "https://www.reddit.com/r/wallstreetbets/comments/uzncgy/most_anticipated_earnings_releases_for_the_week/")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "Reddit post: My Awesome Podcast Episode"
        )
    
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response,"homepage.html")
    
    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "My Awesome Podcast Episode")