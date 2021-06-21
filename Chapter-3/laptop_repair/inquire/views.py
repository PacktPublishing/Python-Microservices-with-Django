from django.shortcuts import render
from django.http import HttpResponse
from inquire.models import Accessorieslist
from booking.models import Orderbook
from django.core import serializers
import json

from response_handler import RespSender
# Create your views here.

# It is used for getting the all available options.
def get_inquire_detail(request):
    aval_option = serializers.serialize("json", Accessorieslist.objects.all())
    aval_option = eval(aval_option)
    resp_send = RespSender()
    response_list = []
    for value in aval_option:
        response_list.append(value['fields'])
    resp = resp_send.send_response("200","Success",response_list)
    return HttpResponse(json.dumps(resp), content_type = 'application/json')


#### http://127.0.0.1:8000/get_booking/details/?booking_id=bid00100

# It is used for getting the all booking detail.
def get_book_details(request):
    book_id = request.GET.get("booking_id")
    aval_option = serializers.serialize("json", Orderbook.objects.filter(booking_id= book_id))
    aval_option = eval(aval_option)
    resp_send = RespSender()
    response_list = []
    if aval_option:
        for value in aval_option:
            response_list.append(value['fields'])
        resp = resp_send.send_response("200","Success",response_list)
    else:
        resp = resp_send.send_response("400","Failed",[{"Error":"Data not found"}])
    return HttpResponse(json.dumps(resp), content_type = 'application/json')