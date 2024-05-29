from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_api_view, name='send_email'),
]