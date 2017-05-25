from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 

def index(request):
    template = get_template('index.html')
    return HttpResponse(template.render(request))