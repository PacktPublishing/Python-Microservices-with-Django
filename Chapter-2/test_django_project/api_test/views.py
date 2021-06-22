from django.shortcuts import render
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)
 
# Create your views here.
def getapi(request):
    # Using the info log to send the message.
    logger.info('Inside the getapi function........')
    return HttpResponse("This is my first GET API")
