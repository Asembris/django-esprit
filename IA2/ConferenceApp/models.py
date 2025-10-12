from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Conference(models.Model):
    conference_id=models.AutoField("coference_id",primary_key=True)
    name=models.CharField("name",max_length=10)
    THEME=[
        ('cs',"Computer Science & Artificial Intelligence"),
        ('sc',"Science & Engineering"),
        ('sce',"Social Sciences & Education"),
        ('i',"Interdisciplinary Themes"),

    ]
    theme=models.CharField("theme",max_length=400,choices=THEME)
    description=models.TextField("description",validators=[MaxLengthValidator(30,'la description doit contenir au maximumm 100 caracteres')])
    location=models.CharField("location",max_length=20)
    start_date=models.DateField("start_date")
    end_date=models.DateField("end_date")
    created_at=models.DateTimeField("created_at",auto_now_add=True)
    updated_at=models.DateTimeField("updated_at",auto_now=True)
    def __str__(self):
        return f"la conference a comme titre  {self.name}"
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("la date de fin ne peut pas etre avant la date de debut")

class Submission(models.Model):
    submission_id=models.CharField(max_length=255,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    abstract=models.TextField()
    keyword=models.TextField()
    paper=models.FileField(
        upload_to="papers/"
    )
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField("created_at",auto_now_add=True)
    updated_at=models.DateTimeField("updated_at",auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
