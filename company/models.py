from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):

    """Company model for Users who are currently Employed"""
    owner = models.OneToOneField(
        User,
        related_name='company'
    )
    logo = models.ImageField(
        upload_to='images/companythumbs/'
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100
    )
    address = models.CharField(
        verbose_name='Address',
        max_length=255
    )
    country = models.CharField(
        verbose_name='Country',
        max_length=100
    )
    province = models.CharField(
        verbose_name='Province',
        max_length=100
    )
    postal_code = models.SmallIntegerField(
        verbose_name='Postal Code',
        default=6000
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    website = models.URLField(
        verbose_name='Website',
        blank=True
    )
    timestamp = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True
    )

    def get_status(self):
        return self.status.get_status()

    def approve(self):
        companystatus = self.status.status = True

    def disallow(self):
        companystatus = self.status.status = False

    def save(self, **kwargs):
        for field in self._meta.fields:
            if field.name == 'logo':
                field.upload_to = 'images/companythumbs/%s' % self.name
        super(Company, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyStatus(models.Model):

    """Status Of A Company"""
    company = models.OneToOneField(
        Company,
        related_name='status'
    )
    status = models.BooleanField(
        verbose_name='Status',
        default=False
    )

    def get_status(self):
        return self.status

    def __unicode__(self):
        return self.get_status()

    def create_company_status(sender, instance, created, **kwargs):
        if created:
            CompanyStatus.objects.create(company=instance)

    class Meta:
        db_table = 'Company_Status'
        verbose_name = 'Company Status'
        verbose_name_plural = 'Company Status'

    models.signals.post_save.connect(create_company_status, sender=Company)
