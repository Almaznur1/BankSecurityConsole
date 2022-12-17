from django.db import models
from datetime import datetime
from datetime import timezone
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

    def get_duration(visit):
        if visit.leaved_at is None:
            current_time = datetime.now(timezone.utc)
            duration = current_time - visit.entered_at
            return duration
        else:
            duration = visit.leaved_at - visit.entered_at
            return duration

    def format_duration(delta):
        hours = floor(delta.total_seconds() / 3600)
        minutes = floor((delta.total_seconds() - 3600 * hours) // 60)
        formatted_duration = f'{hours}ч {minutes}мин'
        return formatted_duration

    def is_visit_long(visit, minutes=60):
        long_visit_in_seconds = 60 * minutes
        if visit.leaved_at is None:
            if (datetime.now(timezone.utc) -
                    visit.entered_at).total_seconds() > long_visit_in_seconds:
                return True
        else:
            if (visit.leaved_at -
                    visit.entered_at).total_seconds() > long_visit_in_seconds:
                return True
        return False
