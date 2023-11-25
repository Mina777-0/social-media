from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Face
from cs50 import SQL
from datetime import datetime

db = SQL("sqlite:///foo.db")


def index(request):
    if request.method == "POST":
        like = request.POST['like']
        date = datetime.now()
        db.execute("INSERT INTO foo (DateTime, Impressions) VALUES(?, ?)",date, like)
    return render(request, "foo/index.html",{'images': Face.objects.all()})
