# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-02 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0030_auto_20180402_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='mailing_list_archive_public',
            field=models.BooleanField(default=False, help_text='Check if the mailing list archive is public'),
        ),
        migrations.AddField(
            model_name='team',
            name='mailing_list_nonmember_posts',
            field=models.BooleanField(default=False, help_text='Check if the mailinglist allows non-list-members to post'),
        ),
    ]