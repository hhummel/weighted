from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime
from .models import Targets, Response

# Create your views here.

def index(request):
    c = {
        "message": "Welcome to w8d!",
    }
    return render(request, 'a/message.html', c)

def redirection(request, target, responder):
    #try:
        obj = Targets.objects.get(index=target)

        print(obj.index, obj.url, target, responder) 

        #Save the reponse event the Response table
        response = Response()
        response.target = obj
        response.respondent = responder
        response.date = datetime.now()
        response.save()

        #Redirect
        return HttpResponseRedirect(obj.url)

    #except Exception:
        message = "Sorry, link was not found on server"
        c = {
            "message": "Sorry, link was not found on server",
        }
        return render(request, 'a/message.html', c)

