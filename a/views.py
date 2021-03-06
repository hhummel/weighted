from re import compile, match
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime
from .models import Targets, Response

# Create your views here.

def index(request):
    c = {
        "message": "Welcome to w8d!",
    }
    return render(request, 'a/balls.html', c)

def test(request):
    c = {
        "message": "Test message",
    }
    return render(request, 'a/message.html', c)

def redirection(request, target, responder):
    '''Key for anonymous respondent is ! target == 0 means don't redirect'''
    #Make matching pattern for responder
    p = compile('^[a-zA-Z0-9]+$')

    if target == 0:
        return index(request)
    try:
        obj = Targets.objects.get(index_key=target)

        #Save reponse event if not anonymous
        response = Response()
        response.target = obj
        if responder != '!' and p.match(responder):
            response.respondent = responder
            response.date = datetime.now()
            response.save()

        #Redirect
        return HttpResponseRedirect(obj.url)

    except Exception:
        c = {
            "message": "Sorry, link was not found on server target=" + target,
        }
        return render(request, 'a/message.html', c)

def responder_redirection(request, responder):
    from w8d.passwords import SUBDOMAIN
    return redirection(request, SUBDOMAIN, responder)

def default_redirection(request):
    from w8d.passwords import SUBDOMAIN
    return redirection(request, SUBDOMAIN, None)

