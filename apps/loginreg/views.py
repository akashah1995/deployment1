# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'loginreg/index.html')

def success(request):
    userid = request.session['userid']
    user = User.objects.get(id = userid)
    context = {
        'user':user
    }
    return render(request, 'loginreg/success.html', context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        
        return redirect(index)
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        User.objects.create(first_name = firstname, last_name = lastname, email = email, password = hash1)

        request.session['userid'] = User.objects.get(email = email).id

        print request.session['userid']

        return redirect(success)

def login(request):
    
    try:
        User1 = User.objects.get(email = request.POST['email'])
    
    except:
        messages.error(request, "Login Failed", extra_tags = "loginerror")
        return redirect(index)

    password = request.POST['password']

    passwordcorrect = User1.password

    print password

    if bcrypt.checkpw(password.encode(), passwordcorrect.encode()):
        messages.error(request, "Login Succesful", extra_tags = "loginerror")
        return redirect(success)

    
    #     request.session['userid'] = User1.id
    #     messages.error(request, "Login Successful!", extra_tags = "loginerror")
    #     return redirect(success)

    # messages.error(request, "Incorrect password", extra_tags = "loginerror")
    
    return redirect(index)









    
    
