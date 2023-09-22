from . import views
from django.urls import path

app_name = 'commenting'

urlpatterns = [
    path('comment/<int:ticket_id>/', views.commet, name='commet'),
    path('comments/<int:ticket_pk>/',views.ListComments.as_view(),name='commetlist')

]
