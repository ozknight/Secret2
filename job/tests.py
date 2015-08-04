import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Hiring


class HiringMethodTest(TestCase):

    def test_for_future_hiring_due(self):
        '''should be true when the set due date is in the future'''
        time = timezone.now() + datetime.timedelta(days=30)
        Future_Due = Hiring(due=time)
        self.assertTrue(Future_Due.valid_for_hiring())

    def test_for_present_hiring_due(self):

        '''should return True When Due Date is the Current Date'''
        time = timezone.now()
        Current_Due = Hiring(due=time)
        self.assertTrue(Current_Due.valid_for_hiring())

    def test_for_past_hiring_due(self):

        '''should return False when due date is over'''
        time = timezone.now() - datetime.timedelta(days=1)
        Current_Due = Hiring(due=time)
        self.assertFalse(Current_Due.valid_for_hiring())
