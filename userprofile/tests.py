import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile
from company.models import Company

Fiftheen_Year = datetime.timedelta(days=365) * 15


def Setup_User():
    user = User(username='test')
    user.save()
    return user


class UserProfile_TestCase(TestCase):

    def test_for_age_below_standard(self):
        """Test For Underage Users"""
        user = Setup_User()
        profile = Profile(user=user, birthdate=datetime.date.today())
        self.assertEquals(profile.valid_age(), False)

    def test_for_age_equals_standard(self):
        """Test For Users With Valid Age Level"""
        user = Setup_User()
        age = datetime.date.today() - Fiftheen_Year
        profile = Profile(user=user, birthdate=age)
        self.assertEquals(profile.valid_age(), True)

    def test_for_age_above_standard(self):
        """Test For Users With Above Valid Age Level"""
        user = Setup_User()
        age = datetime.date.today() - (Fiftheen_Year * 2)
        profile = Profile(user=user, birthdate=age)
        self.assertEquals(profile.valid_age(), True)

    def test_for_no_age(self):
        """Test For Users With No Age"""
        user = Setup_User()
        profile = Profile(user=user)
        self.assertEquals(profile.valid_age(), False)

    def test_for_male_user(self):
        """Test for Male Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='M')
        self.assertEquals(profile.valid_gender(), True)

    def test_for_female_user(self):
        """Test for Female Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='F')
        self.assertEquals(profile.valid_gender(), True)

    def test_for_not_valid_gender_user(self):
        """Test for Female Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='D')
        self.assertEquals(profile.valid_gender(), False)

    def test_for_no_gender_user(self):
        """Test for No Gender Users"""
        user = Setup_User()
        profile = Profile(user=user)
        self.assertEquals(profile.valid_gender(), False)

    def test_for_male_gender_verbose_return(self):
        """Test For 'M' Gender returns Male"""
        user = Setup_User()
        profile = Profile(user=user, gender='M')
        self.assertEquals(profile.get_gender(), 'Male')

    def test_for_female_gender_verbose_return(self):
        """Test For 'F' Gender returns Female"""
        user = Setup_User()
        profile = Profile(user=user, gender='F')
        self.assertEquals(profile.get_gender(), 'Female')

    def test_for_invalid_gender_verbose_return(self):
        """Test For invalid Gender returns 'Not A Human'"""
        user = Setup_User()
        profile = Profile(user=user, gender='X')
        self.assertEquals(profile.get_gender(), 'Not A Human')

    def test_for_user_not_employer(self):
        """test for employer without company"""
        user = Setup_User()
        profile = Profile(user=user)
        self.assertEquals(profile.is_employer(), False)

    def test_for_user_employer(self):
        """test for employer without company"""
        user = Setup_User()
        profile = Profile(user=user, employer=True)
        self.assertEquals(profile.is_employer(), True)

    def test_for_employer_without_company(self):
        """test for employer without company"""
        user = Setup_User()
        profile = Profile(user=user, employer=True)
        self.assertEquals(profile.have_company(), False)

    def test_for_employer_with_company(self):
        """test for employer without company"""
        user = Setup_User()
        profile = Profile(user=user, employer=True)
        self.assertEquals(profile.have_company(), False)
        Company(owner=user).save()
        self.assertEquals(profile.have_company(), True)
