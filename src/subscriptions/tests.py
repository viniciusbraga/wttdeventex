# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscriptionTest(TestCase):
    def test_get_url_subscribe(self):
        response = self.client.get( r('subscriptions:subscribe') )
        self.assertEquals(200, response.status_code)

    def test_get_url_success(self):
        response = self.client.get( r('subscriptions:success', args=[1]) )
        self.assertEquals(200, response.status_code)

    def test_get_view_success(self):
        "Ao visitar /inscricao/ a página de inscrição é exibida."
        response = self.client.get( r('subscriptions:subscribe') )
        self.assertEquals(200, response.status_code)

    def test_use_template_subscribe(self):
        "Não encontrou o template da inscrição."
        response = self.client.get( r('subscriptions:subscribe') )
        self.assertTemplateUsed(response, 'subscriptions/subscription_form.html')


