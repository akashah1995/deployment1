from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect

def index(request):
    try:
        request.session['total'] = request.session['total']
    except:
        request.session['total'] = 0
    
    try:
        request.session['bought'] = request.session['bought']

    except:
        request.session['bought'] = 0
    
    return render(request,'amadon/index.html')

def buy(request):

    request.session['cost'] = 0

    request.session['total'] = request.session['total'] + int(request.POST['quantity'])

    request.session['cost'] = float(request.POST['quantity']) * float(request.POST['cost'])

    request.session['bought'] = float(request.session['bought']) + float(request.session['cost'])


    print request.session['cost']
    print request.session['total']
    print request.session['bought']

    # request.session['cost'] = 0
    # request.session['total'] = 0
    # request.session['bought'] = 0

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def back(request):
    return redirect('/amadon/')

def leave(request):
    request.session['cost'] = 0
    request.session['total'] = 0
    request.session['bought'] = 0
    print request.session['cost']
    return redirect('/amadon/')




    

    

# Create your views here.
