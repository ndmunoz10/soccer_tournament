from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import loader

from stadiums.models import Stadium


@login_required(login_url='/login/', redirect_field_name=None)
def get_stadiums(request):
    stadium_list = Stadium.objects.order_by("code")
    template = loader.get_template("stadiums/index.html")
    context = {
        "stadium_list": stadium_list
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def add_stadium(request):
    if request.method == 'POST':
        form_data = request.POST
        stadium = Stadium(
            code=form_data['code'],
            name=form_data['name'],
            opening_year=form_data['opening_year'],
            capacity=form_data['capacity']
        )
        stadium.save()
        return redirect('/stadiums')


@login_required(login_url='/login/', redirect_field_name=None)
def search_stadium(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        stadium_list = Stadium.objects.filter(name__contains=user_input)
        template = loader.get_template("stadiums/index.html")
        context = {
            "stadium_list": stadium_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/stadiums')


@login_required(login_url='/login/', redirect_field_name=None)
def delete_stadium(request, stadium_id):
    Stadium.objects.get(pk=stadium_id).delete()
    return redirect('/stadiums')
