# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    data = Course.objects.all().values()

    context = {
        'data':data
    }

    return render(request, 'courses/index.html', context)

def addcourse(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(index)

    else: 
        name = request.POST['name']
        description = request.POST['description']

        Course.objects.create(name = name, description = description)
        return redirect(index)

def deletepage(request,variable):

    print variable
    course = Course.objects.get(id = variable)

    context = {
        'course':course
    }

    return render(request, 'courses/deletepage.html',context)

def remove(request, variable):
    course = Course.objects.get(id = variable)
    course.delete()

    return redirect(index)

def back(request):

    return redirect(index)






            




