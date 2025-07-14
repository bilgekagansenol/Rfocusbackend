from django.db import models
from django.utils import timezone


class StudySession(models.Model):
    """
    Model representing a study session.
    This model is used to track study sessions, including the user,"""
    ## user = models.ForeignKey('auth.User', on_delete=models.CASCADE) ## FUTURE WORK 
    title = models.CharField(max_length=100, default="Odak Oturumu")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(default=25) 
    is_completed = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.user.username} - {self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"

