from django.db import models
from django.contrib.auth.models import User
from Ticketing.models import Ticket


# Create your models here.
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.commenter}'
