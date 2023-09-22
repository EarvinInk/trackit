from django.shortcuts import render
from .forms import CommentForm
from Ticketing.models import Ticket
from django.views.generic import ListView
# Create your views here.
from .models import Comment
from django.http import HttpResponse

def commet(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.content=request.POST.get('content')
        comment.commenter = request.user
        comment.ticket = ticket
        comment.save()
        comments = Comment.objects.filter(ticket =ticket)
        return HttpResponse(comments)

    return render(request, 'comment.html', {'form': form})


class ListComments(ListView):
    model = Comment
    # queryset = Comment.objects.filter(ticket = ticket__ticket_id__)
    context_object_name = 'Comments'
    template_name = 'comments.html'
    def get_queryset(self):
        return Comment.objects.filter(ticket = self.kwargs['ticket_pk'])