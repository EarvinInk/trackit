from django.db.models import Q
from django.shortcuts import render
from Ticketing.models import Ticket
from datetime import datetime as dt


# Create your views here.

def search(request):
    querry = None
    tickets = Ticket.objects.all().filter(assigned_to=request.user)
    if request.GET.get('today'):
        tickets = tickets.filter(date_raised__date=dt.now().date())

    if 'qs' in request.GET:
        querry = request.GET.get('qs')
        tickets = tickets.filter(Q(description__icontains=querry) | Q(title__icontains=querry))
    return render(request, 'search.html', {'Querry': querry, 'tickets': tickets})


def adv_search(request):
    tickets = Ticket.objects.all()
    querry = None
    if request.GET.get('title'):
        querry = request.GET.get('title')
        tickets = tickets.filter(title__icontains=querry)
    if request.GET.get('description'):
        querry = request.GET.get('description')
        tickets = tickets.filter(description__icontains=querry)
    if request.GET.get('today'):
        tickets = tickets.filter(date_raised__date=dt.now().date())
    else:
        if request.GET.get('date_min'):
            date = request.GET.get('date_min')
            tickets = tickets.filter(date_raised__date__gte=date)
        if request.GET.get('date_max'):
            date = request.GET.get('date_max')
            tickets = tickets.filter(date_raised__date__lt=date)

    return render(request, 'advsearch.html', {'querry': querry, 'tickets': tickets})