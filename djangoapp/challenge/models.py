from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Challenge(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # start = models.DateTimeField()
    # end = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(
        User,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True
    )

    def __str__(self):
        return self.name


class Activity(models.Model):
    WALKING = 'WALKING'
    CYCLING = 'CYCLING'
    RUNNING = 'RUNNING'
    ACTIVITIES = [
        (WALKING, 'Walking'),
        (CYCLING, 'Cycling'),
        (RUNNING, 'Running')
    ]
    KM = 'KM'
    MILES = 'MILES'
    DISTANCE_MEASURE = [(KM, 'Km'), (MILES, 'Miles')]
    challenges = models.ManyToManyField(
        Challenge,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activity = models.CharField(
        max_length=20, choices=ACTIVITIES, default=CYCLING)
    distance = models.DecimalField(max_digits=6, decimal_places=1, default=0.0)
    measure = models.CharField(
        max_length=5, choices=DISTANCE_MEASURE, default=MILES)
    hours = models.PositiveIntegerField(default=0)
    minutes = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(60)])
    seconds = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(59)])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity
