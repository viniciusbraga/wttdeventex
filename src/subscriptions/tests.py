# coding: utf-8

from django.test import TestCase


class SubscriptionTest(TestCase):
    def test_get_subscribe_instance(self):
        response = self.client.get('/inscricao/')
        self.assertEquals(200, response.status_code)

    def test_get_success_instance(self):
        response = self.client.get('/inscricao/1/')
        self.assertEquals(200, response.status_code)
