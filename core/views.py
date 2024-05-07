from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()
    return HttpResponse(now)
