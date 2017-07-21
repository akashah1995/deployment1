from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from time import gmtime, strftime
import datetime

def index(request):
    try:
        request.session['data'] = request.session['data']
    except:
        request.session['data'] = list()
    
    return render(request, 'session_words/index.html')

def submit(request):
    if request.method == 'POST':

        # try:
        #     request.session['word'] = request.session['word']
        
        # except:
        #     request.session['word'] = list()

        print "made it to submit"

        word = request.POST['word']
        color = request.POST['color']

        print color
        
        try:
            style = request.POST['style']
            
        except:
            style = "regular"
        
        date = str(datetime.datetime.now())
        
        data = {
            'word':word,
            'color':color,
            'style':style,
            'time': date
        }

        request.session['data'].append(data)
        request.session.modified = True
    
        print request.session['data']

        return redirect('/session_words/result')
    else:
        return redirect('/session_words/result')

def result(request):
    return render(request,'session_words/result.html')

def reset(request):
    request.session['data'] = []
    return redirect('/session_words/')
    





# Create your views here.
