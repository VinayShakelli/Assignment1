from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import operator
def home(requests):
    return HttpResponse('<h1> This is my first Assignment</h1>')
def aboutus(requests):
    return HttpResponse('<h1> I am studying B.E. 3rd year in Vasavi College of Engineering </h1>')
def hobbies(requests):
    return HttpResponse('<h1> My hobbies are watching cricket, football, Web series</h1>')

