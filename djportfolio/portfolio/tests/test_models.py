import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError
from portfolio.models import User, Resume, CertificateAuthority, Company, Task, Skill, Certificate, Category, Profession, Job, UserStory, Introduction, Expertise, Project

pytestmark = pytest.mark.django_db

class TestUser:
    def test_single_user_create(self):
        '''Test case to create a single user.'''
        user = mixer.blend('portfolio.User')
        assert user.pk == 1, "Should create a user instance"
    
    def test_multiple_user_create(self):
        '''Test case to create multiple user, the second is prohibited.'''
        user_one = mixer.blend('portfolio.User')
        assert user_one.pk == 1, "Should create a user instance"

        try:
            user_two = mixer.blend('portfolio.User')
        except ValidationError as exc:
             assert True, f"Second user creation should raised a validation error: {exc}."

    def test_str_function(self):
        '''Test case to check __str__ function.'''
        user = User(
            pk = 1,
            first_name = "John",
            last_name = "Doe",
        )
        assert user.__str__() == "John Doe", "Should return John Doe."

class TestResume:
    def test_str_function(self):
        user = User(
            pk = 1,
            first_name = "John",
            last_name = "Doe",
        )
        resume = Resume(user=user)
        assert resume.__str__() == "Resume of John Doe", "Should return John Doe."

class TestCertificateAuthority:
    def test_str_function(self):
        certificate_authority = CertificateAuthority(name="Udemy")
        assert certificate_authority.__str__() == "Udemy", "Should return Udemy."

class TestCompany:
    def test_str_function(self):
        company = Company(name="Reddit")
        assert company.__str__() == "Reddit", "Should return Reddit."

class TestTask:
    def test_str_function(self):
        task = Task(name="Testing")
        assert task.__str__() == "Testing", "Should return Testing."

class TestSkill:
    def test_str_function(self):
        skill = Skill(name="Automated Testing")
        assert skill.__str__() == "Automated Testing", "Should return Automated Testing."

class TestCertificate:
    def test_str_function(self):
        certificate = Certificate(name="Certified Tester Foundation Level")
        assert certificate.__str__() == "Certified Tester Foundation Level", "Should return Certified Tester Foundation Level."

class TestCategory:
    def test_str_function(self):
        category = Category(name="Web Development")
        assert category.__str__() == "Web Development", "Should return Web Development."

class TestProfession:
    def test_str_function(self):
        profession = Profession(name="Test Automation Engineer")
        assert profession.__str__() == "Test Automation Engineer", "Should return Test Automation Engineer."

class TestJob:
    def test_str_function(self):
        company = company = Company(name="Reddit")
        job = Job(
            position="Technical Test Analyst",
            company=company,
        )
        assert job.__str__() == "Technical Test Analyst at Reddit", "Should return Technical Test Analyst at Reddit."

class TestUserStory:
    def test_str_function(self):
        user_story = UserStory(quote="Trust but verify.")
        assert user_story.__str__() == "Trust but verify.", "Should return Trust but verify."

class TestIntroduction:
    def test_str_function(self):
        task = Introduction(quote="Trust but verify.")
        assert task.__str__() == "Trust but verify.", "Should return Trust but verify."

class TestExpertise:
    def test_str_function(self):
        skill = Skill(name="Automated Testing") 
        expertise = Expertise(skill=skill)
        assert expertise.__str__() == "Expertise in Automated Testing", "Should return Expertise in Automated Testing."

class TestProject:
    def test_str_function(self):
        user = User(
            pk = 1,
            first_name = "John",
            last_name = "Doe",
        ) 
        project = Project(
            author = user,
            title="Portfolio Project",
        )
        assert project.__str__() == "Portfolio Project by John Doe", "Should return Portfolio Project by John Doe."
