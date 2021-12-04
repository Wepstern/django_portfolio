import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from .. import views
from django.core.exceptions import ObjectDoesNotExist
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_anonymus_user_in_db_invalid(self):
        request = self.factory.get('/')
        request.user = self.user

        try:
            response = views.index(request)
        except ObjectDoesNotExist as exc:
             assert True, f"Should not be callable without any user. {exc}"

    def test_anonymus_user_in_db_valid(self):
        user = mixer.blend('portfolio.User')
        assert user.pk == 1, 'Should create a user instance'

        request = self.factory.get('/')
        request.user = self.user

        response = views.index(request)
        assert response.status_code == 200, 'Should not be callable without user.'
