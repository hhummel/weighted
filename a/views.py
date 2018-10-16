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

def redirection(request, target, responder):
    '''Key for anonymous respondent is ! target == 0 means don't redirect'''
    if target == 0:
        return index(request)
    try:
        obj = Targets.objects.get(index=str(target))

        #Save the reponse event the Response table
        response = Response()
        response.target = obj
        if responder != '!':
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

