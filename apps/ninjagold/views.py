from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from django.utils.crypto import get_random_string
from random import randint
import datetime

def index(request):
    try: 
        request.session['gold'] = request.session['gold']
    except:
        request.session['gold'] = 0
    
    try: 
        request.session['activities'] = request.session['activities']
    
    except:
        request.session['activities'] = list()

    
    return render(request, 'ninjagold/index.html')

def gold(request):
    
    goldearned = randint(-50,50)
    date = str(datetime.datetime.now())
    if goldearned > 0:
        earnings = {
            'color':'green',
            'amount': goldearned,
            'time':date
        }

    else:
        earnings = {
            'color':'red',
            'amount':goldearned,
            'time':date
        }
    
    request.session['activities'].append(earnings)

    request.session['gold'] = earnings['amount'] + request.session['gold']

    return redirect('/ninjagold/')


# Create your views here.
