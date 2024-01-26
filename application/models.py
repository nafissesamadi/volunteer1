from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpRequest
from django.shortcuts import render

from account.models import PublicPlace, Profile, Volunteer
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# region course_related models
class EducationalLevel(models.Model):
    edu_level = models.CharField(max_length=20, unique=True, verbose_name="دوره آموزشی")
    url_title = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.edu_level


class Grade(models.Model):
    edu_level = models.ForeignKey(EducationalLevel, on_delete=models.CASCADE)
    grade_name = models.CharField(max_length=20, verbose_name="پایه تحصیلی")
    url_title = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.edu_level} {self.grade_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['edu_level', 'grade_name'], name='unique_edu_level_grade')]


class CourseName(models.Model):
    course_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.course_name}"


class Major(models.Model):
    major = models.CharField(max_length=20, unique=True)
    url_title = models.CharField(max_length=100, blank=True, null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.major}"


class Course(models.Model):
    course_name = models.ForeignKey(CourseName, on_delete=models.CASCADE, db_index=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
    image=models.ImageField(upload_to='images/courses', null=True,blank=True)
    code=models.CharField(max_length=7, blank=True, null=True)
    book_download_link=models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f" {self.grade} / {self.course_name} "

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_name', 'grade', 'major'],
                                    name='unique_course_name_edu_level_grade'),
        ]


# endregion


# region time_related models

class WeekDay(models.Model):
    day_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.day_name}"


class AvailableTime(models.Model):
    day_name = models.ForeignKey(WeekDay, on_delete=models.CASCADE, default="1")
    time_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.time_name} / {self.day_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['day_name', 'time_name'], name='unique_day_name_time_name'),
        ]


# endregion

# region skill_related models


class SkillType(models.Model):
    title = models.CharField(max_length=30, unique=True)


class Skill(models.Model):
    skill_name = models.CharField(max_length=500)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.skill_name


# endregion

# region public places models


class SchoolType(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class School(PublicPlace):
    school_type = models.ForeignKey(SchoolType, on_delete=models.CASCADE, blank=True, null=True)
    school_level = models.ForeignKey(EducationalLevel, on_delete=models.CASCADE, blank=True, null=True)
    educational_district = models.IntegerField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.school_level})"


class VenueType(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class ClassVenue(PublicPlace):
    venue_type = models.ForeignKey(VenueType, on_delete=models.CASCADE, null=True, blank=True)
    available_time = models.ManyToManyField(AvailableTime)
    short_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# endregion

# region volunteer & student
class EducationalVolunteer(Volunteer):
    offered_course = models.ManyToManyField(Course)
    edu_level = models.ForeignKey(EducationalLevel, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Preferred Level')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Preferred Grade')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Preferred Major')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    slug = models.SlugField(default="", null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.user})"


class SkilledVolunteer(Volunteer):
    offered_skill = models.ManyToManyField(Skill)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.offered_skill}"


class Student(Profile):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    edu_level = models.ForeignKey(EducationalLevel, on_delete=models.CASCADE, blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    free_time = models.ManyToManyField(AvailableTime)
    special_condition = models.CharField(max_length=10, blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.user}"


# endregion

# region application_related models
HOLDING_STYLE = [
    ("V", "مجازی"),
    ("FTF", "حضوری"),
]


class Application(models.Model):
    objects = None
    applicant = models.ManyToManyField(Student)
    demanded_course = models.ForeignKey(Course, on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    preferred_style = models.CharField(choices=HOLDING_STYLE, max_length=50, null=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    is_accepted = models.BooleanField(blank=True, null=True, default=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    registered_date = models.DateField(null=True, blank=True , auto_now_add=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, default="", null=False, db_index=True)



    def get_absolute_url(self):
        # return reverse('application_detail', args=[self.slug])
        return reverse('application_detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.demanded_course)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.demanded_course}"


class AcceptedApplication(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    edu_volunteer = models.ForeignKey(EducationalVolunteer, on_delete=models.CASCADE, blank=True, null=True)
    class_venue = models.ForeignKey(ClassVenue, on_delete=models.CASCADE)
    holding_time = models.ManyToManyField(AvailableTime)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.application}({self.edu_volunteer})"
# endregion

