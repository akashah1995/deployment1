from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from time import gmtime, strftime
import datetime

def index(request):
    # context = {"time": strftime("%b %d %Y %I:%M %p", gmtime())}
    context = {"time": datetime.datetime.now()}
    return render(request, 'timedisplay/index.html', context)

# Create your views here.
