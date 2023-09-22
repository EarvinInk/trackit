from .models import Ticket
from django.db.models import Q, Count
from datetime import datetime as dt

def counter(request):
    return Ticket.objects.aggregate(
        # total=Count('pk', filter=Q(assigned_to=request.user) & Q(date_raised__date = dt.now().date())),
        closed=Count('pk', filter=Q(progress=1) & Q(date_raised__date = dt.now().date())),
        raised=Count('pk', filter=Q(progress=0) & Q(date_raised__date = dt.now().date())),
        in_progress=Count('pk', filter=Q(progress=2) & Q(date_raised__date = dt.now().date())),
        low=Count('pk', filter=Q(priority=1) & Q(date_raised__date = dt.now().date())),
        medium=Count('pk', filter=Q(priority=2) & Q(date_raised__date = dt.now().date())),
        high=Count('pk', filter=Q(priority=3) & Q(date_raised__date = dt.now().date())),
    )
