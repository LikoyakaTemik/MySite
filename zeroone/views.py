from django.shortcuts import render
import sqlite3 as sq
from django.db import models
from django.conf import settings
import socket
from .models import counter
time = {"times": 0}


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def Menu(request):
    if request.method == "GET":
        checker = list(counter.objects.filter(ip_user=str(get_ip())))
        if len(checker) == 0:
            counter.objects.create(ip_user=str(get_ip()), ind=0)
            data = {"times": 0}
            return render(request, "Menu.html", data)
        else:
            data = {"times": int(checker[0].ind)}
            return render(request, "Menu.html", data)
    if request.method == "POST":
        checker = list(counter.objects.filter(ip_user=str(get_ip())))
        checker[0].ind = int(checker[0].ind) + 1
        checker[0].save()
        data = {"times": checker[0].ind}
        return render(request, "Menu.html", data)


def gradient(request):
    if request.method == "GET":
        return render(request, "gradient.html")
    elif request.method == "POST":
        return render(request, "gradient.html")


def animations(request):
    if request.method == "GET":
        return render(request, "animations.html")
    elif request.method == "POST":
        return render(request, "animations.html")

def alien(request):
    if request.method == "GET":
        return render(request, "alien.html")
    elif request.method == "POST":
        return render(request, "alien.html")

def tests(request):
    if request.method == "GET":
        return render(request, "tests.html")
    elif request.method == "POST":
        return render(request, "tests.html")