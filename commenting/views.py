from django.shortcuts import render
from .forms import CommentForm
from Ticketing.models import Ticket
from django.views.generic import ListView
# Create your views here.
from .models import Comment


def commet(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commenter = request.user
        comment.ticket = ticket

        comment.save()
    return render(request, 'comment.html', {'form': form})


class ListComments(ListView):
    model = Comment
    # queryset = Comment.objects.filter(ticket = ticket__ticket_id__)
    context_object_name = 'Comments'
    template_name = 'Comments.html'
    def get_queryset(self):
        return Comment.objects.filter(ticket = self.kwargs['ticket_pk'])