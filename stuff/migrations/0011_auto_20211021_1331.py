# Generated by Django 3.2.7 on 2021-10-21 13:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0010_alter_challenges_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='challenge_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='challenges',
            name='solved_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='disliked_challenges',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='liked_challenges',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, null=True), null=True, size=None),
        ),
    ]
