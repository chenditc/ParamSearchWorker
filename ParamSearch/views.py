from django.shortcuts import render
from django.http import HttpResponse

import json
import logging
import sklearn

logger = logging.getLogger("ParamSearch")

# Create your views here.
def index(request):
    logger.info("Request:{0}".format(request))

    # Do stuff
    return HttpResponse(json.dumps("ok"), content_type="application/json")

def health(request):
    logger.info("Health check")
    return HttpResponse(json.dumps("ok"), content_type="application/json")
