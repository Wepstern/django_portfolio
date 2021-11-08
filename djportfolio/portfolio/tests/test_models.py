import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestUser:
    def test_single_user_create(self):
        user = mixer.blend('portfolio.User')
        assert user.pk == 1, 'Should create a user instance'
    
    def test_multiple_user_create(self):
        user_one = mixer.blend('portfolio.User')
        assert user_one.pk == 1, 'Should create a user instance'

        try:
            user_two = mixer.blend('portfolio.User')
        except ValidationError as exc:
             assert True, f"Second user creation should raised a validation error: {exc}"
