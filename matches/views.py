from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect
from django.template import loader

from matches.models import Match, Goal, FreeKick, Fault, Change


@login_required(login_url='/login/', redirect_field_name=None)
def get_matches(request):
    match_list = Match.objects.order_by("date")
    template = loader.get_template("matches/index.html")
    context = {
        "match_list": match_list
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def search_match(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        match_list = Match.objects.filter(home_team_name__contains=user_input)
        template = loader.get_template("matches/index.html")
        context = {
            "match_list": match_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/matches')


@login_required(login_url='/login/', redirect_field_name=None)
def delete_match(request, match_id):
    Match.objects.get(pk=match_id).delete()
    return redirect('/matches')


@login_required(login_url='/login/', redirect_field_name=None)
def get_match_stats(request, match_id):
    goal_list = Goal.objects.order_by('player_name')
    free_kick_list = FreeKick.objects.order_by('shooter_name')
    fault_list = Fault.objects.order_by('reason')
    change_list = Change.objects.order_by('in_player_name')
    away_team_name = Match.objects.get(pk=match_id).away_team_name
    home_team_name = Match.objects.get(pk=match_id).home_team_name
    template = loader.get_template('matches/stats.html')
    context = {
        'goal_list': goal_list,
        'free_kick_list': free_kick_list,
        'fault_list': fault_list,
        'change_list': change_list,
        'away_team_name': away_team_name,
        'home_team_name': home_team_name
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def add_match(request):
    if request.method == 'POST':
        form_data = request.POST
        goal = Goal(
            player_name=form_data['scorer_name'],
            minute=form_data['goal_minute'],
            team=form_data['goal_team_name']
        )
        free_kick = FreeKick(
            shooter_name=form_data['shooter_name'],
            barrier_names=form_data['barrier_names'],
            team_name=form_data['free_kick_team_name']
        )
        fault = Fault(
            reason=form_data['fault_reason'],
            minute=form_data['fault_minute'],
            team_name=form_data['fault_team_name'],
            card=form_data['card']
        )
        change = Change(
            in_player_name=form_data['in_player_name'],
            out_player_name=form_data['out_player_name'],
            minute=form_data['change_minute'],
            team_name=form_data['change_team_name']
        )
        match = Match(
            goal=goal,
            free_kick=free_kick,
            fault=fault,
            change=change,
            home_team_name=form_data['home_team_name'],
            away_team_name=form_data['away_team_name'],
            stadium_name=form_data['stadium_name'],
            date=form_data['date'],
            start_time=form_data['time'],
            away_team_score=form_data['away_team_score'],
            home_team_score=form_data['home_team_score']
        )
        goal.save()
        free_kick.save()
        fault.save()
        change.save()
        match.save()
        return redirect('/matches')
