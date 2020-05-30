from django.shortcuts import render,HttpResponse
from django.urls import resolve
import json
# Create your views here.
import logging
db_logger = logging.getLogger('db')

db_logger.info('info message')
db_logger.warning('warning message')

try:
    1/0
except Exception as e:
    db_logger.exception(e)

def hello(request):
    current_url = resolve(request.path_info).url_name
    if request.method=='GET':

        try:
            return render(request,'molly/index.html')
        except Exception as ex:
            msg = json.dumps({'path':request.path_info,'exception':str(ex)})
            db_logger.exception(msg)
            return HttpResponse()
