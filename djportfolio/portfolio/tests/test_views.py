import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from .. import views
from mixer.backend.django import mixer
from django.test import Client
import time

pytestmark = pytest.mark.django_db

class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_index_error_700(self):
        user_one = mixer.blend('portfolio.User')
        user_two = mixer.blend('portfolio.User')
        client = Client()
        response = self.client.get('')
        assert response.context['error'] == 700, 'Error code should be 700.'

    def test_index_error_701(self):
        client = Client()
        response = self.client.get('')
        assert response.context['error'] == 701, 'Error code should be 701.'
    
    def test_index_send_contact_form(self):
        user_= mixer.blend('portfolio.User')
        client = Client()
        response = client.post('', {
            'Contact': '',
            'contact_message': 'Hello friend. Hello friend? That\'s lame. Maybe I should give you a name.', 
            'contact_email': 'test@test.com'}
        )
        assert response.status_code == 302, 'Should redirect.'

    def test_index_open(self):
        user_= mixer.blend('portfolio.User')
        client = Client()
        response = client.get('')
        assert response.status_code == 200, 'Should redirect.'
    