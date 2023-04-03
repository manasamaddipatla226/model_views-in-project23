from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from app.models import Book

# Create your views here.
def title(request):
    return HttpResponse(input('enter a string here'))
    