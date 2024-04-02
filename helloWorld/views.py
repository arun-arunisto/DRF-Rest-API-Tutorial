from django.shortcuts import render
from django.http import JsonResponse
from . models import Sample


# Create your views here.
def hello_world(request):
    data = {
        "Api Name":"Hello World",
        "Method":"hello_world",
        "endpoint":"/api/hello-world-api/hello-world"
    }
    return JsonResponse(data)

def fetch_all_data(request):
    sample_data = Sample.objects.all()
    data = {
        "Api Name":"Hello World",
        "Method":"fetch_all_data",
        "endpoint":"/api/hello-world-api/fetch-all-data",
        "Fetch data":list(sample_data.values())
    }

    return JsonResponse(data)

def fetch_single_data(request, id):
    single_data = Sample.objects.get(id=id)
    data = {
        "Api Name": "Hello World",
        "Method": "fetch_all_data",
        "endpoint": "/api/hello-world-api/fetch-single-data/"+str(id)+"/",
        "Fetch data":[{
            "Name":single_data.name,
            "Age":single_data.age,
            "Job":single_data.job,
            "Created At":single_data.created_at
        }]
    }
    return JsonResponse(data)
