from . import views
from django.urls import path

app_name = 'ticket'

urlpatterns = [
    path('', views.Ticketview.as_view(), name='home'),
    path('create', views.create_ticket, name='create'),
    path('close/<int:ticket_id>/', views.close_ticket, name='close'),
    path('edit/<int:pk>/', views.EditTicket.as_view(), name='edit'),
    path('detail/<int:pk>/', views.TicketDetails.as_view(), name='detail'),
    path('raise/<int:ticket_id>/', views.priority_raise, name='raise'),
    path('lower/<int:ticket_id>/', views.priority_lower, name='lower'),
]
