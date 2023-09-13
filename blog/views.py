from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
