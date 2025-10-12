from email.policy import default
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def generate_user_id():
    return 'USER'+uuid.uuid4().hex[:4].upper()

def validate_user_email(email):
    domaines=['esprit.tn','sesame.com','tekup.tn','contract.net']
    if not any(email.endswith(domaine) for domaine in domaines):
        raise ValidationError('email non valide')

name_validator=RegexValidator(regex=r'^[a-zA-Z\s]+$',message='nom et prenom ne doivent contenir que des lettres et des espaces')



class User(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name=models.CharField(max_length=255,validators=[name_validator])
    last_name=models.CharField(max_length=255,validators=[name_validator])
    ROLE=[
        ('participant','participant'),
        ('comitee','organizing comitee member'),
    ]
    role=models.CharField(max_length=255,choices=ROLE,default="participant")
    affiliation=models.CharField(max_length=255)
    email=models.EmailField(unique=True,validators=[validate_user_email])
    nationality=models.CharField(max_length=255)
    created_at=models.DateTimeField("created_at",auto_now_add=True)
    updated_at=models.DateTimeField("updated_at",auto_now=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            new_id = generate_user_id()
            while User.objects.filter(user_id=new_id).exists():
                new_id = generate_user_id()
            self.user_id = new_id
        super().save(*args, **kwargs)


class OrganizingComitee(models.Model):
    comitee_role=models.CharField(max_length=255,choices=[
        ("chair","chair"),
    ])
    join_date=models.DateField()
    created_at=models.DateTimeField("created_at",auto_now_add=True)
    updated_at=models.DateTimeField("updated_at",auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="comitees")
    conference=models.ForeignKey("ConferenceApp.Conference",on_delete=models.CASCADE,related_name="comitees")


