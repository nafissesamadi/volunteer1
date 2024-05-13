from django.db import models
from django.contrib.auth.models import AbstractUser
from smart_selects.db_fields import ChainedForeignKey



# Create your models here.

# region location_related classes
class Province(models.Model):
    name = models.CharField(max_length=500)
    url_title = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=500)
    url_title = models.CharField(max_length=100, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    parent_city = models.ForeignKey("self", related_name="child_cities", null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# endregion


# region user-related models

GENDER_TYPES = (
    ("F", "بانو"),
    ("M", "آقا"),
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


NATIONALITY = (
    ("IR", "ایرانی"),
    ("F", "اتباع"),
)

class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, verbose_name='Code Melli', unique=True, blank=True, null=True)
    gender = models.CharField(choices=GENDER_TYPES, max_length=10, default="F")
    last_password_reset_on = models.DateTimeField(auto_now_add=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    city = ChainedForeignKey(
        City, on_delete=models.CASCADE,
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(choices=NATIONALITY, max_length=300, default="IR")

    # address=models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.user}"



class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education_degree = models.CharField(choices=EDUCATION_DEGREE, max_length=10, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    work_experience = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=2000, default="", null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


# endregion

# region Public place model

class PublicPlaceType(models.Model):
    title = models.CharField(max_length=30, unique=True)
    url_title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class PublicPlace(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(PublicPlaceType, on_delete=models.CASCADE,blank=True, null=True)
    director = models.OneToOneField(User, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = ChainedForeignKey(
        City, on_delete=models.CASCADE,
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        sort=True)
    district= models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return f"{self.name}  ({self.province}/{self.city}/{self.district})"


# endregion
