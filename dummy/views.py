from django import http
from django.shortcuts import render
from dummy.models import Dummy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
def dummy(request):
    return http.HttpResponse("I'm Dummy", status = 200)

def allDummies(request):
    dummies = Dummy.objects.all()
    return http.HttpResponse(serializers.serialize('json', dummies), 
                             content_type = 'application/json', status = 200)

@csrf_exempt
def createDummy(request):
    if request.method == 'POST':
        dummy = Dummy.objects.create(name = request.POST.get('name'))
        dummy.save()    
        return http.HttpResponse(dummy, content_type = 'application/json', status = 201)