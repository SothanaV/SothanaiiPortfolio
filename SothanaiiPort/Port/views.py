# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html')
def sothana(request):
	return render(request,'first.html')
def study(request):
	return render(request,'study.html')
def reward(request):
	return render(request,'reward.html')
def activity(request):
	return render(request,'activity.html')
def tarlent(request):
	return render(request,'tarlent.html')
def port(request):
	return render(request,'port.html')
def work(request):
	return render(request,'work.html')