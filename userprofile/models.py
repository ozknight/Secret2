from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from company.models import Company
from django.utils import timezone

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)
MIN_VALID_AGE = 15
Valid_Gender = []
for Gender in GENDER:
    Valid_Gender.append(Gender[0])
    Valid_Gender.sort()


class Profile(models.Model):

    """User Profile Model"""
    user = models.OneToOneField(
        User
    )
    avatar = models.ImageField(
        upload_to='images/userthumbs/',
        blank=True
    )
    birthdate = models.DateField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        blank=True
    )
    phone = models.CharField(
        verbose_name='Contact #:',
        max_length=16,
        blank=True
    )
    about_you = models.TextField(
        verbose_name='About You :',
        blank=True
    )
    employer = models.BooleanField(
        default=False,
        blank=True
    )

    def is_employer(self):
        return self.employer

    def is_Profile_Set(self):
        if self.is_gender_valid() and self.is_valid_user_age() and self.about_you:
            return True
        return False

    def is_valid_user_age(self):
        if not self.birthdate:
            return False
        age = timezone.now().year - self.birthdate.year
        return age >= MIN_VALID_AGE

    def is_gender_valid(self):
        if self.gender in Valid_Gender:
            return True
        return False

    def User_Created_A_Company(self):
        try:
            company = Company.objects.get(owner=self.user)
        except Company.DoesNotExist:
            return False
        return True

    def check_company(self):
        try:
            company = Company.objects.get(owner=self.user)
        except ObjectDoesNotExist:
            company = 'False'
        return company

    def save(self, **kwargs):
        for field in self._meta.fields:
            if field.name == 'avatar':
                field.upload_to = 'images/userthumbs/%d' % self.user.id
        super(Profile, self).save()

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __unicode__(self):
        return self.user.username + "\'s Profile"

    class Meta:
        db_table = 'User_Profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    is_employer.boolean = True
    models.signals.post_save.connect(create_user_profile, sender=User)
