from django.contrib.auth.models import User
from django.db import models

LOW = 1
MED = 2
HIGH = 3
PRIORITIES = [(LOW, 'LOW'), (MED, 'MEDIUM'), (HIGH, 'HIGH')]  # LIMIT PRIORITY CHOICES,

RAISED = 0
IN_PROGRESS = 2
CLOSED = 1
PROGRESS = [(RAISED, 'RAISED'), (IN_PROGRESS, 'IN PROGRESS'), (CLOSED, 'CLOSED')]


class Ticket(models.Model):
    product = models.CharField(max_length=100)
    priority = models.IntegerField(choices=PRIORITIES)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raised_by')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to', default="Unassigned")
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='closed_by', null=True)

    progress = models.IntegerField(choices=PROGRESS)
    description = models.TextField()
    date_raised = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    closed_on = models.DateTimeField(null=True)
    time_taken = models.DurationField(null=True)
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date_raised',)
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

