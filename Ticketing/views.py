from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView, ListView, DetailView
from .models import Ticket
from django.contrib.auth.models import User
from datetime import datetime as dt
from .forms import TicketForm


# Create your views here.

def create_ticket(request):
    if request.method == 'POST':
        priority = request.POST['priority']
        description = request.POST['description']
        title = request.POST['title']
        ticket = Ticket(priority=priority,
                        progress=0,
                        description=description,
                        raised_by=request.user,
                        title=title
                        )
        ticket.save()
        return redirect('/')
    return render(request, 'create_ticket.html')


def close_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.progress = 1
    ticket.closed_on = dt.now().replace(microsecond=0)
    ticket.time_taken = ticket.closed_on - ticket.date_raised.replace(tzinfo=None)
    ticket.closed_by = request.user
    ticket.save()
    return HttpResponse(ticket.get_progress_display())


def priority_raise(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.priority < 3:
        ticket.priority += 1
    else:
        ticket.priority = 3
    ticket.save()
    return HttpResponse(ticket.get_priority_display())


def priority_lower(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.priority > 1:
        ticket.priority -= 1
    else:
        ticket.priority = 1
    ticket.save()
    return HttpResponse(ticket.get_priority_display())


class EditTicket(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'edit_ticket.html'
    context_object_name = 'ticket'

    # fields = ['priority', 'progress']

    def get_success_url(self):
        return reverse('ticket:home')


class TicketView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'home.html'


class TicketDetails(DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'
