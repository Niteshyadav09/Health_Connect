# Generated by Django 4.1.7 on 2023-04-05 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0006_insurancedetails_verified_medicaldetails_verified'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('organ_affected', models.CharField(max_length=100)),
                ('disease_serious', models.IntegerField(default=1)),
                ('doctor', models.CharField(max_length=100)),
                ('treatment', models.CharField(max_length=100)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('treatment_done', models.BooleanField(default=False)),
                ('treatment_time', models.IntegerField(default=-1)),
                ('survived', models.BooleanField(default=True)),
                ('insured', models.BooleanField(default=False)),
                ('medicalinst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userauth.medicaldetails')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('doctor', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userauth.medicaldetails')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
