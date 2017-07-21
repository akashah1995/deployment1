# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from models import *

def create(request):
    
    return render(request, 'restful/create.html')

def add(request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    User.objects.create(first_name = str(firstname), last_name = str(lastname), email = str(email))

    return redirect(index)

def index(request):

    data = User.objects.all().values()

    context = {
        'data' : data
    }

    print context


    return render(request, 'restful/index.html',context)

def addpage(request):
    return redirect(create)

def back(request):
    return redirect(index)

def show(request,variable):
    print variable
    
    data = User.objects.get(id = variable)
    print data

    context = {
        'data': data
    }

    return render(request, 'restful/show.html',context)

def edit(request,variable):
    print variable

    context = {
        'data':variable
    }

    return render(request, 'restful/edit.html',context)

def update(request):

    pointer = User.objects.get(id = request.POST['id'])
    
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    pointer.first_name = firstname
    pointer.save()
    pointer.last_name = lastname
    pointer.save()
    pointer.email = email
    pointer.save()



    return redirect(index)

def delete(request,variable):
    pointer = User.objects.get(id = variable)
    pointer.delete()

    return redirect(index)




    
    


# Create your views here.
