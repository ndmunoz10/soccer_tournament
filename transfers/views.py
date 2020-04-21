from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import loader

from transfers.models import Transfer


@login_required(login_url='/login/', redirect_field_name=None)
def get_transfers(request):
    transfer_list = Transfer.objects.order_by("name")
    template = loader.get_template("transfers/index.html")
    context = {
        "transfer_list": transfer_list
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/', redirect_field_name=None)
def add_transfer(request):
    if request.method == 'POST':
        form_data = request.POST
        transfer = Transfer(
            name=form_data['name'],
            old_team_name=form_data['old_team_name'],
            new_team_name=form_data['new_team_name'],
            price=form_data['price']
        )
        transfer.save()
        return redirect('/transfers')


@login_required(login_url='/login/', redirect_field_name=None)
def search_transfer(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        transfer_list = Transfer.objects.filter(name__contains=user_input)
        template = loader.get_template("transfers/index.html")
        context = {
            "transfer_list": transfer_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/transfers')


@login_required(login_url='/login/', redirect_field_name=None)
def delete_transfer(request, transfer_id):
    Transfer.objects.get(pk=transfer_id).delete()
    return redirect('/transfers')
