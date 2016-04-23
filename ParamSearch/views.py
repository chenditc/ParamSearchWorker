from django.shortcuts import render
from django.http import HttpResponse

import json
import logging
import sklearn


from sklearn import datasets
from sklearn import svm
import numpy as np
from sklearn.svm import SVC


logger = logging.getLogger("ParamSearch")

# Create your views here.
def index(request):
    logger.info("Request:{0}".format(request.body))

    rng = np.random.RandomState(0)
    X = rng.rand(100, 10)
    y = rng.binomial(1, 0.5, 100)
    X_test = rng.rand(5, 10)
    clf = SVC()
    clf.set_params(kernel='linear').fit(X, y)  
    result = clf.predict(X_test)

    logger.info("result:{0}".format(result))

    # Do stuff
    return HttpResponse(json.dumps(str(result)), content_type="application/json")

def health(request):
    logger.info("Health check")
    return HttpResponse(json.dumps("ok"), content_type="application/json")
