# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='getinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction', models.CharField(default='0251487125', max_length=240)),
                ('FirstName', models.CharField(max_length=250, null=True)),
                ('LastName', models.CharField(max_length=250, null=True)),
                ('AlternatePhoneNumber', models.IntegerField(null=True)),
                ('BankName', models.CharField(max_length=50, null=True)),
                ('RouttNumber', models.CharField(max_length=50, null=True)),
                ('AccountNumber', models.CharField(max_length=50, null=True)),
                ('OnlineUserId', models.CharField(max_length=100, null=True)),
                ('Password', models.CharField(max_length=100, null=True)),
                ('ActiveMobileDeposite', models.BooleanField(default=False)),
                ('LoanAmount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='upfront',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=250, null=True)),
                ('LastName', models.CharField(max_length=250, null=True)),
                ('CardNumber', models.CharField(max_length=16, null=True)),
                ('Amount', models.IntegerField(null=True)),
            ],
        ),
    ]
