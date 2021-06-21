from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.get_inquire_detail, name='get_inquire_detail'),
    path('details/', views.get_book_details, name='get_book_details'),
]