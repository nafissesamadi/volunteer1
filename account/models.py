from django.db import models
from django.contrib.auth.models import AbstractUser
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

# region location_related classes
class Province(models.Model):
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, default="", null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=500)
    province = models.ForeignKey(Province, related_name="state", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    parent_city = models.ForeignKey(
        "self",
        related_name="child_cities",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


# endregion
# region user-related models


GENDER_TYPES = (
    ("F", "Female"),
    ("M", "Male"),
)

MARTIAL_STATUS = (
    ("Single", "Single"),
    ("Married", "Married"),
)

EDUCATION_DEGREE = [
    ("UG", "Under Graduate"),
    ("B", "BACHELOR"),
    ("M", "MASTER"),
    ("PHD", "PHD"),
]


class UserType(models.Model):
    objects = None
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Job(models.Model):
    job_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.job_name


class User(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name='mobile')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email Activation code')
    mobile_verification_code = models.CharField(max_length=50, null=True, blank=True, default="")
    mobile_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.user_type})"


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, verbose_name='Code Melli', unique=True, blank=True, null=True)
    gender = models.CharField(choices=GENDER_TYPES, max_length=10, blank=True, null=True)
    last_password_reset_on = models.DateTimeField(auto_now_add=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City,null=True, blank=True, on_delete=models.CASCADE)

    # address=models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.user}"



class Volunteer(Profile):
    education = models.CharField(choices=EDUCATION_DEGREE, max_length=10, null=True, blank=True)
    marital_status = models.CharField(choices=MARTIAL_STATUS, max_length=50, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    job_role = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    work_experience = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=2000, default="", null=True, blank=True)

    class Meta:
        abstract = True


# endregion

# region abstract place model

class PublicPlace(models.Model):
    name = models.CharField(max_length=200)
    director = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return f"{self.name}"
    


# endregion
