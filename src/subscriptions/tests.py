# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.db import IntegrityError
from .models import Subscription
from .forms import SubscriptionForm

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

    def test_has_form(self):
        "A resposta deve conter o formulário de inscrição."
        self.assertIsInstance(self.resp.context['form'], SubscriptionForm)

    def test_form_has_fields(self):
        "O formulário deve conter os campos: name, email, cpf e phone"
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_html(self):
        "O html deve conter os campos do formulário"
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

class SubscriptionModelTeste(TestCase):

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

class SubscribeViewPostTest(TestCase):

    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='00000000000', email='vini@vini.com', phone='21-96186180')
        self.resp = self.client.post( r('subscriptions:subscribe'), data )

    def test_redirects(TestCase):
        "Post deve redirecionar para a página de sucesso."
        self.assertRedirects( self.resp, r('susbcriptions:success', args=[1]) )

    def test_save(self):
        "Post deve salvar Subscription no banco."
        self.assertTrue(Subscription.objects.exists())

class SubscribeViewInvalidPostTest(TestCase):

    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='000000000001', email='vini@vini.com', phone='21-96186180')
        self.resp = self.client.post( r('subscriptions:subscribe'), data )

    def test_show_page(self):
        "Post inválido não deve redirecionar."
        self.assertEqual(200, self.resp.status_code)

    def test_form_erros(self):
        "Form deve conter erros."
        self.assertTrue(self.resp.context['form'].errors)

    def test_must_not_save(self):
        "Dados não devem ser salvos"
        self.assertFalse( Subscription.objects.exists() )



