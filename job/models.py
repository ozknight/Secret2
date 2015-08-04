import datetime
from django.db import models
from company.models import Company
from django.utils import timezone

STATUS_CHOICE = (
    ('A', 'Accept'),
    ('R', 'Reject'),
    ('P', 'Pending')
)
STATUS_VALUE = []
for status in STATUS_CHOICE:
    STATUS_VALUE.append(status[0])
    STATUS_VALUE.append(status[1])


class JobCategory(models.Model):

    '''Job Category Model'''
    name = models.CharField(verbose_name='Job Category', max_length=255)
    description = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Category:' + str(self.name)

    class Meta:
        db_table = 'Job_Categories'
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'


class JobType(models.Model):

    '''Sets Of Job Type for Hiring Classification Purposes'''
    name = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Type:' + str(self.name)

    class Meta:
        db_table = 'Job_Types'
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'


class Hiring(models.Model):

    '''Job Hiring Model'''
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirement = models.TextField()
    timestamp = models.DateTimeField(verbose_name='Posted', auto_now_add=True)
    category = models.ForeignKey(JobCategory, related_name='category')
    job_type = models.ForeignKey(JobType, related_name='type')
    due = models.DateField('Due Date')
    status = models.BooleanField(default=True)

    def valid_for_hiring(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.due

    def __unicode__(self):
        return self.title + " by " + str(self.company)

    class Meta:
        db_table = 'Job_Hirings'
        verbose_name = 'Hiring'
        verbose_name_plural = 'Hirings'
