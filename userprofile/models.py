from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
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
    Valid_Gender.append(Gender[1])


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

    def get_gender(self):
        if self.valid_gender():
            return_id=Valid_Gender.index(self.gender) + 1
            return Valid_Gender[return_id]
        return 'Not A Human'

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return '/static/images/userthumbs/default.png'

    def is_employer(self):
        return self.employer

    def is_Profile_Set(self):
        if self.valid_gender() and self.valid_age():
            return True
        return False

    def valid_age(self):
        if not self.birthdate:
            return False
        age = timezone.now().year - self.birthdate.year
        return age >= MIN_VALID_AGE

    def valid_gender(self):
        if self.gender in Valid_Gender:
            return True
        return False

    def have_company(self):
        try:
            company = self.user.company
        except Exception:
            return False
        return True

    def save(self, **kwargs):
        for field in self._meta.fields:
            if field.name == 'avatar':
                field.upload_to = 'images/userthumbs/%d' % self.user.id
        super(Profile, self).save()

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def clean(self):
        if not self.valid_age():
            raise ValidationError({'birthdate': ['Underage Applicant!']})

    def __unicode__(self):
        return self.user.username + "\'s Profile"

    class Meta:
        db_table = 'User_Profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    is_employer.boolean = True
    models.signals.post_save.connect(create_user_profile, sender=User)
