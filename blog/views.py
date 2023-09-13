from django.shortcuts import render
from django import HttpResponse


def Home(response):
    return HttpResponse('<h1>Blog Home</h1>')
