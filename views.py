from django.views.generic import ListView

from .models import Reddit
from .models import Episode

class HomePageView(ListView):
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:100]
        return context


# Create your views here.
