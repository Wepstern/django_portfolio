# import os
# from pathlib import Path
# from selenium import webdriver
# import selenium
# from selenium.webdriver.chrome import service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from .. import models
# from .. import views
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse
# import time
# from mixer.backend.django import mixer
# import pytest

# pytestmark = pytest.mark.django_db

# BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# chrome_driver = os.path.join(BASE_DIR, 'utils', 'chromedriver')

# class TestUserProfile(StaticLiveServerTestCase):

#     def setUp(self):
#         self.service = Service(chrome_driver)
#         self.browser = webdriver.Chrome(service=self.service)

#     def tear_down(self):
#         self.browser.close()
    
#     def test_user_in_db_invalid(self):
#         longMessage = True

#         self.browser.get(self.live_server_url)

#         alert = self.browser.find_element(By.TAG_NAME,'h1')
#         self.assertEqual(
#             alert.text, 'Server Error (500)', 'Should be appeared a server error 500 page'
#         )

#         self.tear_down()
    
#     def test_user_in_db_valid(self):
#         longMessage = True

#         #Create user
#         user = mixer.blend('portfolio.User')
#         assert user.pk == 1, 'Should create a user instance'

#         #Open browser
#         self.browser.get(self.live_server_url)

#         #Check user name
#         user_name = self.browser.find_element(By.CLASS_NAME,'test-user-name')
#         self.assertEqual(
#             user_name.text, "{} {}".format(user.last_name, user.first_name), 'Should be appeared user name'
#         )

#         #Check user profession
#         user_profession = self.browser.find_element(By.CLASS_NAME,'test-user-profession')
#         self.assertEqual(
#             user_profession.text, "{}".format(user.profession), 'Should be appeared user profession'
#         )

#         #Check user profile picture
#         default_picture = self.browser.find_element(By.CLASS_NAME,'test-user-profile-picture')
#         self.assertEqual(
#             default_picture.get_attribute("src"), "{}/{}".format(self.live_server_url, user.profile_picture), 'Should be appeared default profile picture link'
#         )
        
#         #Check user profile picture position
#         location = default_picture.location

#         ref_x = 711
#         self.assertEqual(
#             location['x'], ref_x, "Should be px the profile picture x postion".format(ref_x)
#         )
#         ref_y = 244
#         self.assertEqual(
#             location['y'], ref_y, "Should be 160 px the profile picture y postion".format(ref_y)
#         )

#         #Check user profile picture size
#         size = default_picture.size

#         ref_width = 300
#         self.assertEqual(
#             size['width'], ref_width, "Should be 300 px the profile picture width".format(ref_width)
#         )

#         ref_height = 300
#         self.assertEqual(
#             size['height'], ref_height, "Should be 300 px the profile picture height".format(ref_height)
#         )

#         #Check navigator elements - Home
#         nav_home = self.browser.find_element(By.CLASS_NAME, 'test-nav-home')
#         self.assertEqual(
#             nav_home.text, 'Home', 'Should be called \'Home\''
#         )

#         self.assertEqual(
#             nav_home.get_attribute('href'), "{}/{}".format(self.live_server_url, '#home'), 'Should be href #home'
#         )

#         home_link_by_tag_name = self.browser.find_element(By.TAG_NAME, 'body')
#         body_id = home_link_by_tag_name.get_attribute('id')
#         self.assertEqual(
#             body_id, '#home', 'Should the body have the #home id'
#         )

#         #Check navigator elements - About
#         nav_about = self.browser.find_element(By.CLASS_NAME, 'test-nav-about')
#         self.assertEqual(
#             nav_about.text, 'About', 'Should be called \'About\''
#         )

#         self.assertEqual(
#             nav_about.get_attribute('href'), "{}/{}".format(self.live_server_url, '#about'), 'Should be href #about'
#         )

#         #Check navigator elements - Expertise
#         nav_expertise = self.browser.find_element(By.CLASS_NAME, 'test-nav-expertise')
#         self.assertEqual(
#             nav_expertise.text, 'Expertise', 'Should be called \'Expertise\''
#         )

#         self.assertEqual(
#             nav_expertise.get_attribute('href'), "{}/{}".format(self.live_server_url, '#expertise'), 'Should be href #expertise'
#         )

#         #Check navigator elements - Experience
#         nav_experience = self.browser.find_element(By.CLASS_NAME, 'test-nav-experience')
#         self.assertEqual(
#             nav_experience.text, 'Experience', 'Should be called \'Experience\''
#         )

#         self.assertEqual(
#             nav_experience.get_attribute('href'), "{}/{}".format(self.live_server_url, '#experience'), 'Should be href #experience'
#         )

#         #Check navigator education - Education
#         nav_education = self.browser.find_element(By.CLASS_NAME, 'test-nav-education')
#         self.assertEqual(
#             nav_education.text, 'Education', 'Should be called \'Education\''
#         )

#         self.assertEqual(
#             nav_education.get_attribute('href'), "{}/{}".format(self.live_server_url, '#education'), 'Should be href #education'
#         )

#         #Check navigator education - Contact
#         nav_contact = self.browser.find_element(By.CLASS_NAME, 'test-nav-contact')
#         self.assertEqual(
#             nav_contact.text, 'Contact', 'Should be called \'Contact\''
#         )

#         self.assertEqual(
#             nav_contact.get_attribute('href'), "{}/{}".format(self.live_server_url, '#contact'), 'Should be href #contact'
#         )

#         self.tear_down()

#         # TODO:
#         # - sections & links
#         # - view my portfolio button
#         # - social media profile
#         # - 
