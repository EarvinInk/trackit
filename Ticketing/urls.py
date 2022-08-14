from . import views
from django.urls import path

app_name = 'ticket'

urlpatterns = [
    path('', views.Ticketview.as_view(), name='viewall'),
    path('create', views.create_ticket, name='Create'),
    path('close/<int:ticket_id>/', views.close_ticket, name='Close ticket'),
    path('edit/<int:pk>/', views.Edit_ticket.as_view(), name='Edit ticket')
]
