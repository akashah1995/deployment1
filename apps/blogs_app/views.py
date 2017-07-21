from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect

def index(request):
    response = "placeholder to later display all the list of blogs!"
    return HttpResponse(response)

def new(request):
    another = "placeholder to display a new form to create a new blog!"
    return HttpResponse(another)

def create(request):
    return redirect(request,'/blogs')

def show(request,number):
    response = "placeholder to display blog number " + number + " "
    return HttpResponse(response)

def edit(request,number):
    response = "placeholder to edit blog number " + number + " "
    return HttpResponse(response)

def destroy(request):
    return redirect(request,'/')







# Create your views here.
