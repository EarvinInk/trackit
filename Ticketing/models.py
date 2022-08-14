
from django.db import models


# Create your models here.
# ticket model
class Ticket(models.Model):
    low = 1
    med = 2
    high = 3
    PRIORITIES = [(low, 'Low'), (med, 'Medium'), (high, 'High')]  # limit priority choices,
    product = models.CharField(max_length=100)
    priority = models.IntegerField(choices=PRIORITIES)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    raised = 0
    in_progress = 2
    closed = 1
    PROGRESS = [(raised, 'Raised'), (in_progress, 'In Progress'), (closed, 'Closed')]
    progress = models.IntegerField()
    description = models.TextField()
    date_raised = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    closed_on = models.DateTimeField()
    time_taken = models.DurationField()
    comments = models.TextField()

    class Meta:
        ordering = ('-date_raised',)
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
