from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . handler import Host


def index(request):
    return HttpResponse(Host().get_name())
