from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # start = models.DateTimeField()
    # end = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # members = models.ManyToManyField(
    #     User,
    #     related_name="%(app_label)s_%(class)s_related",
    #     related_query_name="%(app_label)s_%(class)ss",
    # )


class ChallengeActivity(models.Model):
    WALKING = 'WALKING'
    CYCLING = 'CYCLING'
    RUNNING = 'RUNNING'
    ACTIVITIES = [
        (WALKING, 'Walking'),
        (CYCLING, 'Cycling'),
        (RUNNING, 'Running')
    ]
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    activity = models.CharField(max_length=20, choices=ACTIVITIES, default=CYCLING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
