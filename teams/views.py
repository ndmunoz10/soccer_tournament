from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import loader

from teams.models import Team, City, Sponsor


@login_required(login_url='/login/', redirect_field_name=None)
def get_teams(request):
    team_list = Team.objects.order_by("creation_year")
    template = loader.get_template("teams/index.html")
    context = {
        "team_list": team_list
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def search_team(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        team_list = Team.objects.filter(name__contains=user_input)
        template = loader.get_template("teams/index.html")
        context = {
            "team_list": team_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/teams')


@login_required(login_url='/login/', redirect_field_name=None)
def get_team_stats(request, team_id):
    city_list = City.objects.order_by('name')
    sponsor_list = Sponsor.objects.order_by('name')
    team_name = Team.objects.get(pk=team_id).name
    template = loader.get_template('teams/stats.html')
    context = {
        'city_list': city_list,
        'sponsor_list': sponsor_list,
        'team_name': team_name,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def add_team(request):
    if request.method == 'POST':
        form_data = request.POST
        city = City(
            name=form_data['city_name'],
            population_size=form_data['population_size']
        )
        sponsor = Sponsor(
            name=form_data['sponsor_name'],
            legal_representative=form_data['legal_representative'],
            email=form_data['email'],
            origin_city=form_data['origin_city']
        )
        team = Team(
            name=form_data['team_name'],
            creation_year=form_data['creation_year'],
            city=city,
            sponsor=sponsor
        )
        city.save()
        sponsor.save()
        team.save()
        return redirect('/teams')


@login_required(login_url='/login/', redirect_field_name=None)
def delete_team(request, team_id):
    Team.objects.get(pk=team_id).delete()
    return redirect('/teams')
