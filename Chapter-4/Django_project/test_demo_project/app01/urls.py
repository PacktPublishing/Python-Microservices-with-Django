from django.urls import path

from . import views

urlpatterns = [
    path('emp_details/', views.get_employee_details, name='get_employee_details'),
]