from django.db import models

# Create your models here.
class job(models.Model):
    Designation=models.CharField(max_length=240)
    company_name=models.CharField(max_length=240)
    job_description=models.CharField(max_length=240)
    Starting_date=models.DateField()
    search_count=models.IntegerField(default=0)
    def __str__(self):
        return self.job_description
