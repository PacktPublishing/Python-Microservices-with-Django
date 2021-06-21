from django.urls import path

from . import views

urlpatterns = [
    path('confirm/', views.confirm_booking, name='confirm_booking'),
]