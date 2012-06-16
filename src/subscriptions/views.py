# coding: utf-8

from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse as r

from .forms import SubscriptionForm

def subscribe(request):
  if request.method == 'POST' :
    form = SubscriptionForm(request.POST)
    if form.is_valid():
      subscription = form.save()
      return HttpResponseRedirect ( r('subscriptions:success', args=[subscription.pk]) )
  else:
    form = SubscriptionForm()

  return direct_to_template( request, 'subscriptions/subscription_form.html', { 'form': form } )

def success(request, pk):
  return HttpResponse()