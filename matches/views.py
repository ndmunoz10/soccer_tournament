from django.http import HttpResponse

# Create your views here.
from django.template import loader

from matches.models import Match


def get_matches(request):
    fight_list = Match.objects.order_by("date")
    template = loader.get_template("matches/index.html")
    context = {
        "match_list": fight_list
    }
    return HttpResponse(template.render(context, request))
