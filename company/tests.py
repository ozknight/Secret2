from django.contrib.auth.models import User
from django.test import TestCase
from .models import Company, CompanyStatus


def Setup_User():
    user = User(username='test')
    user.save()
    return user


class Company_TestCase(TestCase):

    """Test Cases for Company Models"""
    def test_for_getting_logo(self):
        """Test Get Logo Url for New Company Without Logo"""
        user = Setup_User()
        company = Company(owner=user)
        company.save()
        self.assertEquals(company.get_logo(), 'static/comanythumbs/default.png')

    def test_new_company_status(self):
        """Test New Created Company"""
        user = Setup_User()
        company = Company(owner=user)
        company.save()
        CompanyStatus(company=company)
        self.assertEquals(company.get_status(), False)

    def test_for_approved_company(self):
        """Test for Approved Company"""
        user = Setup_User()
        company = Company(owner=user)
        company.save()
        CompanyStatus(company=company)
        self.assertEquals(company.get_status(), False)
        company.approve()
        self.assertEquals(company.get_status(), True)

    def test_for_disapproved_company(self):
        """Test for Approved Company"""
        user = Setup_User()
        company = Company(owner=user)
        company.save()
        CompanyStatus(company=company)
        self.assertEquals(company.get_status(), False)
        company.approve()
        self.assertEquals(company.get_status(), True)
        company.disallow()
        self.assertEquals(company.get_status(), False)
