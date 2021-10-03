from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(req):
    return render(req,"index.html")