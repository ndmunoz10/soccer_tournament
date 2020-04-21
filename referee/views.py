from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import loader

from referee.models import Referee


@login_required(login_url='/login/', redirect_field_name=None)
def get_referees(request):
    referee_list = Referee.objects.order_by("id_card")
    template = loader.get_template("referee/index.html")
    context = {
        "referee_list": referee_list
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def add_referee(request):
    if request.method == 'POST':
        form_data = request.POST
        referee = Referee(
            id_card=form_data['card_id'],
            tutor=form_data['tutor'],
            name=form_data['name']
        )
        referee.save()
        return redirect('/referees')


@login_required(login_url='/login/', redirect_field_name=None)
def search_referee(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        referee_list = Referee.objects.filter(name__contains=user_input)
        template = loader.get_template("referee/index.html")
        context = {
            "referee_list": referee_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/referees')


@login_required(login_url='/login/', redirect_field_name=None)
def delete_referee(request, referee_id):
    Referee.objects.get(pk=referee_id).delete()
    return redirect('/teams')
