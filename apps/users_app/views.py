from django.shortcuts import render, HttpResponse,HttpResponseRedirect

def index(request):
    response = "placeholder to display all the list of users"
    return HttpResponse(response)

def new(request):
    another = "placeholder for users to create a new user record"
    return HttpResponse(another)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)






# Create your views here.
