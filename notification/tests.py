from django.contrib.auth.models import User
from django.test import TestCase
from .models import Notification


def Setup_User(name):
    user = User(username=name)
    user.save()
    return user

def Setup_Notification(user1, user2):
    note = Notification(creator=user1,
        receiver=user2,
        content="For Testing Purposes"
    )
    note.save()
    return note


'''TestCases For Notification App'''
class Notification_TestCase(TestCase):

    '''Test For Creating A Regular Notification Without A Content'''
    def test_for_setting_new_notification(self):
        user1 = Setup_User("test")
        user2 = Setup_User("test2")
        note = Notification(creator=user1, receiver=user2)
        note.save()
        self.assertTrue(note.is_new())

    '''Test For Creating A Regular Notification With A Content'''
    def test_for_setting_new_notificationified_user(self):
        user1 = Setup_User("test")
        user2 = Setup_User("test2")
        note = Setup_Notification(user1, user2)
        self.assertTrue(note.is_new())

    '''Test For Notified Notice But Unread Message'''
    def test_for_notified_user_but_unread(self):
        user1 = Setup_User("test")
        user2 = Setup_User("test2")
        note = Setup_Notification(user1, user2)
        self.assertTrue(note.is_new())
        note.notified()
        self.assertFalse(note.is_new())
        self.assertTrue(note.is_notified())
        self.assertFalse(note.is_read())

