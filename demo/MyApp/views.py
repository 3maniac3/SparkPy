from django.shortcuts import render
from django.http import HttpResponse

# Web views
def index(response):
	return HttpResponse("<h1>Hello, World!</h1>")
	
def user(response):
	return render(response, "main/base.html", {"content": "Goodbye World."})
