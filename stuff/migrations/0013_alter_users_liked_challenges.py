# Generated by Django 3.2.7 on 2021-10-21 18:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0012_alter_users_liked_challenges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='liked_challenges',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), null=True, size=None),
        ),
    ]
