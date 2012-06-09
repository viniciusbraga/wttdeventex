# coding: utf-8

from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

def subscribe(request):
	return direct_to_template(request, template='subscriptions/subscription_form.html')

def success(request, pk):
	return HttpResponse()