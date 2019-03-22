import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Pro2.settings')
import django
django.setup()
import random
from job.models import job
from faker import Faker
fake=Faker()
def populate(N=10):
    for entry in range(20,40):
        name=fake.company()
        job_description=fake.job()
        date=fake.future_date(end_date="+30d", tzinfo=None)
        job.objects.create(company_name=name,job_description=job_description,Starting_date=date)
if __name__=='__main__':
    populate()
