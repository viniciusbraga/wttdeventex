# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscriptionTest(TestCase):
    def test_get_subscribe_instance(self):
        response = self.client.get( r('subscriptions:subscribe') )
        self.assertEquals(200, response.status_code)

    def test_get_success_instance(self):
        response = self.client.get( r('subscriptions:success', args=[1]) )
        self.assertEquals(200, response.status_code)
