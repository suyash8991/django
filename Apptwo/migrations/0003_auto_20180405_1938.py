# Generated by Django 2.0.2 on 2018-04-05 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apptwo', '0002_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='birth_date',
            field=models.CharField(max_length=222),
        ),
        migrations.AlterField(
            model_name='register',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
