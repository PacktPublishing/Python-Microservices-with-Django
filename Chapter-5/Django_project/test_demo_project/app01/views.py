from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Employee as emp
from django.core import serializers
import json
from response_handler import RespSender

### Url:  http://127.0.0.1:8000/get_data/emp_details/?employee_id=2

# It is used for getting the employee details by Id.
def get_employee_details(request):
    emp_id = request.GET.get("employee_id")
    aval_option = serializers.serialize('json', emp.objects.filter(employee_id=emp_id))
    aval_option = eval(aval_option)
    resp_send = RespSender()
    response_list = []
    if aval_option:
        for value in aval_option:
            response_list.append(value["fields"])
        resp = resp_send.send_response("200","Success",response_list)
    else:
        resp = resp_send.send_response("400","Failed",[{"Error":"Data not found"}])
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
