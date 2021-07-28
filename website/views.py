from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome tho the Meeting Planner!")

def about(request):
    return HttpResponse("This is a line of text in my about page.")