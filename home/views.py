from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    return render(request, 'home/index.html')
