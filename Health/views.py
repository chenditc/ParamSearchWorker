from django.shortcuts import render
from django.http import HttpResponse

import json
import logging

logger = logging.getLogger("Health")

def health(request):
    logger.info("Health check")
    return HttpResponse(json.dumps("ok"), content_type="application/json")
