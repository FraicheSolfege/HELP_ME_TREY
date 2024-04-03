from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def true_or_false(request, num):
    if num >= 90 or num <= 100:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
