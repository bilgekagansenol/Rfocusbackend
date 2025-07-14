from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    ##user = models.OneToOneField(User, on_delete=models.CASCADE) # FUTURE WORK

    name = models.CharField(max_length=100)
    gold = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    # Ekipman
    head = models.CharField(max_length=100, blank=True, null=True)
    armor = models.CharField(max_length=100, blank=True, null=True)
    weapon = models.CharField(max_length=100, blank=True, null=True)
    off_hand = models.CharField(max_length=100, blank=True, null=True)
    ring1 = models.CharField(max_length=100, blank=True, null=True)
    ring2 = models.CharField(max_length=100, blank=True, null=True)
    ring3 = models.CharField(max_length=100, blank=True, null=True)
    pet = models.CharField(max_length=100, blank=True, null=True)

    # Toplam çalışma süresi
    total_work_hour = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
