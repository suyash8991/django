# Generated by Django 2.0.2 on 2018-04-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=240)),
                ('company_name', models.CharField(max_length=240)),
                ('job_description', models.CharField(max_length=240)),
                ('Starting_date', models.DateField()),
            ],
        ),
    ]
