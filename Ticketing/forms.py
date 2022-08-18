from .models import Ticket
from django import forms


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['priority', 'progress']
        widgets = {
            'priority': forms.Select(attrs = {'class':'form-control'}),
            'progress': forms.Select(attrs={'class': 'form-control'})
        }
