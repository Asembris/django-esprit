from tkinter import CASCADE
from django.db import models
from ConferenceApp.models import Conference
from django.core.exceptions import *
from django.core.validators import *
# Create your models here.



class Session(models.Model):
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room = models.CharField(max_length=255,validators=[RegexValidator(regex=r'^[A-Za-z0-9\s]+$', message="Room name must contain only letters and numbers (no special characters).")])
    created_at=models.DateTimeField("created_at",auto_now_add=True)
    updated_at=models.DateTimeField("updated_at",auto_now=True)
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="sessions")
    def verif_start_end_time(self):
        if self.start_time < self.end_time:
            raise ValidationError("Start time must be before end time.")
    def clean(self):
        if self.conference:
            if not (self.conference.start_date <= self.session_day<= self.conference.end_date):
                        raise ValidationError({"session_day": "Session day must be between conference start date and end date."})
            self.verif_start_end_time()
    
