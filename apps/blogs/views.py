# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages

# Create your views here.
def index(request):
    print('entered index')
    # context = {
    #     "email" : "blog@gmail.com",
    #     "name" : "mike"
    # }
    response = "placeholder to display all the list of blogs"
    return HttpResponse(response)
    # return render(request, "blogs/index.html")


def new(request):
    print('entered new')
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print('entered create')
    return redirect('/blogs')

def show(request, number):
    response =  'placeholder to display blog ' + number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + number
    return HttpResponse(response)

def destroy(request, number):
    print('entered delete')
    return redirect('/blogs')

