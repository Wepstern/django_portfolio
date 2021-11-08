import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from .. import models
from .. import views
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from mixer.backend.django import mixer
import pytest

pytestmark = pytest.mark.django_db

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

chrome_driver = os.path.join(BASE_DIR, 'utils', 'chromedriver')

class TestUserProfile(StaticLiveServerTestCase):

    def setUp(self):
        self.service = Service(chrome_driver)
        self.browser = webdriver.Chrome(service=self.service)

    def tear_down(self):
        self.browser.close()
    
    def test_user_in_db_invalid(self):
        longMessage = True

        self.browser.get(self.live_server_url)

        alert = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertEqual(
            alert.text, 'Server Error (500)', 'Should be appeared a server error 500 page'
        )

        self.tear_down()
    
    def test_user_in_db_valid(self):
        longMessage = True

        user = mixer.blend('portfolio.User')
        assert user.pk == 1, 'Should create a user instance'

        self.browser.get(self.live_server_url)

        first_name = self.browser.find_element(By.ID,'firstname')
        self.assertEqual(
            first_name.text, "First name: {}".format(user.first_name), 'Should be appeared user first name'
        )

        last_name = self.browser.find_element(By.ID,'lastname')
        self.assertEqual(
            last_name.text, "Last name: {}".format(user.last_name), 'Should be appeared user last name'
        )

        birth_date = self.browser.find_element(By.ID,'birthdate')
        self.assertEqual(
            birth_date.text, "Birth date: {}".format(user.birth_date), 'Should be appeared user birth date'
        )

        sex = self.browser.find_element(By.ID,'sex')
        self.assertEqual(
            sex.text, "Sex: {}".format(user.sex), 'Should be appeared user sex'
        )

        default_picture = self.browser.find_element(By.ID,'profilepicture')
        size = default_picture.size
        location = default_picture.location

        ref_x = 0
        ref_y = 160
        ref_width = 300
        ref_height = 300

        self.assertEqual(
            default_picture.get_attribute("src"), "{}/static/img/default.jpg".format(self.live_server_url), 'Should be appeared default profile picture'
        )
        self.assertEqual(
            location['x'], ref_x, "Should be px the profile picture x postion".format(ref_x)
        )
        self.assertEqual(
            location['y'], ref_y, "Should be 160 px the profile picture x postion".format(ref_y)
        )
        self.assertEqual(
            size['width'], ref_width, "Should be 300 px the profile picture width".format(ref_width)
        )
        self.assertEqual(
            size['height'], ref_height, "Should be 300 px the profile picture height".format(ref_height)
        )

        self.tear_down()
