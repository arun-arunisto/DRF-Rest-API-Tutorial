from django.shortcuts import render
from .models import AppDetails
# Create your views here.
def index(request):
    data = AppDetails.objects.all().order_by("-id")
    for d in data:
        d.endpoints = d.endpoints.split(",")
    return render(request, "index.html", {"data":data})
