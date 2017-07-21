from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from django.utils.crypto import get_random_string

def index(request):

    try: 
        request.session['randomword'] = request.session['randomword']
    except:
        request.session['randomword'] = ''
    
    return render(request, 'randomword/index.html')

def reset(request):
    print "resetting"
    if request.method == 'POST':
        request.session['randomword'] = get_random_string(length = 14)
        return redirect('/random_word')

    else:
        return redirect('/random_word')

# Create your views here.

# Create your views here.
