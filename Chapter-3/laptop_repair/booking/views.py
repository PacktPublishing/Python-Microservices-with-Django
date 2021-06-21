from django.shortcuts import render
from booking.models import Orderbook
import time
from .froms import Registration
# Create your views here.

def confirm_booking(request):
    fm = Registration(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            first_name = fm.cleaned_data["first_name"]
            last_name = fm.cleaned_data["last_name"]
            laptop_desc = fm.cleaned_data["laptop_desc"]
            booking_date = fm.cleaned_data["booking_date"]
            booking_time = fm.cleaned_data["booking_time"]
            contact_number = fm.cleaned_data["contact_number"]
            address = fm.cleaned_data["address"]
            accessory = fm.cleaned_data["accessory"]
            additional_comment = fm.cleaned_data["additional_comment"]
            booking_id = create_booking_id()
            data_obj = Orderbook(first_name =  first_name,last_name = last_name ,laptop_desc = laptop_desc ,booking_date = booking_date ,booking_time = booking_time ,contact_number = contact_number ,address = address ,accessory  = accessory ,additional_comment = additional_comment ,booking_id = booking_id)
            data_obj.save()
            # It is for sending the response.
            return render(request, 'reply.html', {"reply": booking_id})
    else:
        fm = Registration()
        return render(request, 'check.html', {"form":fm})

# This function is used for generating the booking id.
def create_booking_id():
    book_id = str(int(time.time()))
    return book_id