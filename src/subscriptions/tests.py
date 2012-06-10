# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from .models import Subscription
from django.db import IntegrityError

class SubscriptionsUlrTest(TestCase):

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



class SubscriptionTeste(TestCase):

    def test_create(self):
        'O modelo deve ter os campos : name, cpf, email, phone, created_at'
        s = Subscription.objects.create(
            name = 'Vinicius Braga',
            cpf = '01234567891',
            email = 'vini@vini.com',
            phone = '21-22222222'
            # created_at é automático
        )
        self.assertEquals(s.id, 1)



class SubscriptionModelUniqueTest(TestCase):

    def setUp(self):
        # Cria uma primeira inscrição no banco.
        Subscription.objects.create(
            name = 'Vinicius Braga',
            cpf = '01234567891',
            email = 'vini@vini.com',
            phone = '21-22222222'
            )

    def test_cpf_must_be_unique(self):
        'CPF deve ser único'
        # Instancia a inscrição com o CPF já existente e criado no setUP.
        s = Subscription(
            name = 'Vinicius Braga',
            cpf = '01234567891',
            email = 'outro@vini.com',
            phone = '21-22222222'
            )
        # Verifica se ocorre o erro de integridade ao persistir.
        self.assertRaises(IntegrityError, s.save)

    def test_email_must_be_unique(self):
        'Email deve ser único'
        # Instancia a inscrição com o Email já existente e criado no setUP.
        s = Subscription(
            name = 'Vinicius Braga',
            cpf = '00000000000',
            email = 'vini@vini.com',
            phone = '21-22222222'
            )
        # Verifica se ocorre o erro de integridade ao persistir.
        self.assertRaises(IntegrityError, s.save)

