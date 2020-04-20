from django.http import HttpResponse

# Create your views here.
from django.template import loader

from transfers.models import Transfer


def get_transfers(request):
    transfer_list = Transfer.objects.order_by("name")
    template = loader.get_template("transfers/index.html")
    context = {
        "transfer_list": transfer_list
    }
    return HttpResponse(template.render(context, request))
