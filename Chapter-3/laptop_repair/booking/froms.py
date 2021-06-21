
from django import forms

class Registration(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    laptop_desc = forms.CharField(label="Laptop Name With Model", initial="Macbook pro 16")
    booking_date = forms.CharField(label="Booking Date", initial="01 May 2021")
    booking_time = forms.CharField(label="Time for Booking", initial="10:00 - 11:00 AM")
    contact_number = forms.CharField(label="Your Mobile")
    address = forms.CharField(label="Your Address For Service")
    accessory = forms.CharField(label="Accessory")
    additional_comment = forms.CharField(label="Any Additional Details")