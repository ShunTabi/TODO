from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

def NOW_TIME(req):
    params = {
        "values":datetime.now().strftime("%Y-%m-%d"),
    }
    return JsonResponse(params)