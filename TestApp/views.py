from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testview(request):
    return HttpResponse("This is a test view and url for TestProject")

