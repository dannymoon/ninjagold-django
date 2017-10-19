from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime

def index(request):
    if 'goldcollected' not in request.session:
        request.session['goldcollected'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []
    return render(request, 'ninja/index.html')

def process(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            golds = random.randrange(10,21)
            request.session['goldcollected'] += golds
        if request.POST['place'] == 'cave':
            golds = random.randrange(5,11)
            request.session['goldcollected'] += golds
        if request.POST['place'] == 'house':
            golds = random.randrange(2,6)
            request.session['goldcollected'] += golds
        if request.POST['place'] == 'casino':
            golds = random.randrange(-50,50)
            request.session['goldcollected'] += golds
        if request.POST['place'] == 'reset':
            request.session['goldcollected'] = 0
            request.session['messages'] = []
            return redirect('/')
        if golds > 0:
            earnorlost = 'plus'
        else:
            earnorlost = 'negative'
        activitylog = {'goldcollected':golds,'place':request.POST['place'],'earnorlost':earnorlost, 'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())}
        request.session['messages'].append(activitylog)
    
    return redirect('/')

# Create your views here.
