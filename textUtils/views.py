
from django.http.response import HttpResponse
from django.shortcuts import render
import string


def index(request):
    info = {'name':'Abubaker','address':'Gojra, Punjab, Pakitan'}
    return render(request,'home.html',info)

def analyzetext(request):
    text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase','off')
    capatilize = request.GET.get('capatilize','off')
    spaceremover = request.GET.get('spaceremover','off')
    count = request.GET.get('cpunt','off')
    if removepunc=='on':
        analyzedText = ""
        for char in text:
            if char not in string.punctuation:
                analyzedText = analyzedText + char
        text=analyzedText
    if uppercase=='on':
        text = text.upper()
    if capatilize=='on' and uppercase=='off':
        text = text.capitalize()
    if spaceremover=='on':
        spaceremoved = ""
        for char in text:
            if char!=' ':
                spaceremoved = spaceremoved+char
        text = spaceremoved
    dict = {'analyezedText':text}
    if count=='on':
        counter = "Total letters are" + len(text)
        print(counter)
        dict['count'] = counter
    return render(request,'analyzetext.html',dict)