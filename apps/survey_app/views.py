from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect

def index(request):
    try:
        request.session['count'] = request.session['count']
    except:
        request.session['count'] = 0

    return render(request, "survey_app/index.html")

def new(request):
    if request.method == 'POST':
        request.session['count'] = request.session['count'] + 1
        request.session['name'] = request.POST['yourname']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/surveys/result')
    else:
        return redirect('surveys/result')

def result(request):
    return render(request,'survey_app/submitted.html')

def back(request):
    if request.method == 'POST':
        return redirect('surveys/')
    else:
        return redirect('surveys/')



# Create your views here.
