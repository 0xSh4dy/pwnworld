# Generated by Django 3.2.7 on 2021-09-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0006_auto_20210922_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]