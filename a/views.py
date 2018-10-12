from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    c = {
        "message": "Welcome to w8d!",
    }
    return render(request, 'a/message.html', c)

def redirection(request, target):
    targets = {
        1: 'https://gloriousgrain.com/bread/unsubscribe',
        2: 'https://recyclobuddy.com/app/cancel'
    }

    if target not in targets:
        c = {
            "message": "Sorry, link was not found on server",
        }
        return render(request, 'a/message.html', c)
    else:
        url = targets[target]
        print("Redirected to %s" % url)
        return HttpResponseRedirect(url)

