# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscriptionUlrTest(TestCase):

    def test_get_subscribe_instance(self):
        response = self.client.get( r('subscriptions:subscribe') )
        self.assertEquals(200, response.status_code)

    def test_get_success_instance(self):
        response = self.client.get( r('subscriptions:success', args=[1]) )
        self.assertEquals(200, response.status_code)



class SubscribeViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get_view_success(self):
        "Ao visitar /inscricao/ a página de inscrição é exibida."
        self.assertEquals(200, self.resp.status_code)

    def test_use_template_subscribe(self):
        "Não encontrou o template da inscrição."
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

