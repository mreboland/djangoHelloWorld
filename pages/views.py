# HttpResponse returns a response object to the user.
from django.shortcuts import render, HttpResponse

# Create your views here.

# This function accepts the request object and returns a response with the string given
def homePageView(request):
    return HttpResponse("Hello, World!")
