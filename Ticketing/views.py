from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView, ListView
from .models import Ticket
from django.contrib.auth.models import User
from datetime import datetime as dt


# Create your views here.

def create_ticket(request):
    if request.method == 'POST':
        priority = request.POST['priority']
        description = request.POST['description']
        comment = request.POST['comment']
        ticket = Ticket(priority=priority,
                        progress=0,
                        description=description,
                        assigned_to=request.user,
                        comments=comment
                        )
        ticket.save()
        return redirect('/')
    return render(request, 'create_ticket.html')


def close_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.progress = 1
        ticket.closed_on = dt.now().replace(microsecond=0)
        print(ticket.date_raised)
        print(ticket.closed_on)
        ticket.time_taken = ticket.closed_on - ticket.date_raised.replace(tzinfo=None)
        ticket.closed_by = request.user
        ticket.save()

    return render(request, 'close_ticket.html', {'ticket': ticket})


class Edit_ticket(UpdateView):
    model = Ticket
    template_name = 'edit_ticket.html'
    context_object_name = 'ticket'
    fields = ['priority', 'progress']

    def get_success_url(self):
        return reverse('ticket:viewall')


class Ticketview(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'home.html'
