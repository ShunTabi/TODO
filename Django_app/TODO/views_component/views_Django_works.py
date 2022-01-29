from django.shortcuts import render
from . import views_conf

def index(req):
    return render(req,"index.html")
    
def Django_works(req):
    return render(req, "Django_works.html")

