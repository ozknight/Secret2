from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):

    '''
    Model for Vinna notification app
    '''
    creator = models.ForeignKey(User, related_name='notifications_created')
    receiver = models.ForeignKey(User, related_name='notification_recieved')
    content = models.TextField()
    status = models.BooleanField(blank=True, default=False)
    meta_status = models.BooleanField(blank=True, default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_creator(self):
        return self.creator

    def get_reveiver(self):
        return self.receiver

    def get_content(self):
        return self.content

    def get_stamp(self):
        return self.timestamp

    def is_notified(self):
        if self.meta_status:
            return True
        return False

    def is_read(self):
        if self.status:
            return True
        return False

    def is_new(self):
        if not self.is_notified() and not self.is_read():
            return True
        return False

    def notified(self):
        self.meta_status = True
        self.save()

    def read(self):
        if not self.status:
            self.status = True
            self.notified()

    class Meta:
        db_table = 'Notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
