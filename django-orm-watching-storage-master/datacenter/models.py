from django.db import models
from datetime import datetime, timezone
from math import floor

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def format_duration(delta):
        hours = floor(delta.total_seconds() / 3600)
        minutes = floor((delta.total_seconds() - 3600 * hours) // 60)
        duration = f'{hours}h {minutes}min'
        return duration

    def get_duration(visit):
        current_time = datetime.now(timezone.utc)
        delta = current_time - visit.entered_at
        return delta
 