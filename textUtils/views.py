
from django.http.response import HttpResponse
from django.shortcuts import render
import string


def index(request):
    info = {'name':'Abubaker','address':'Gojra, Punjab, Pakitan'}
    return render(request,'home.html',info)

def analyzetext(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase','off')
    capatilize = request.POST.get('capatilize','off')
    spaceremover = request.POST.get('spaceremover','off')
    if spaceremover=='on' or removepunc=='on' or capatilize=='on' or uppercase=='on':
        if removepunc == 'on':
            analyzedText = ""
            for char in text:
                if char not in string.punctuation:
                    analyzedText = analyzedText + char
            text = analyzedText
        if uppercase == 'on':
            text = text.upper()
        if capatilize == 'on' and uppercase == 'off':
            text = text.capitalize()
        if spaceremover == 'on':
            spaceremoved = ""
            for char in text:
                if char != ' ':
                    spaceremoved = spaceremoved + char
            text = spaceremoved
    else:
        text = "No Operation Selected"
    dict = {'analyezedText':text}
    return render(request,'analyzetext.html',dict)