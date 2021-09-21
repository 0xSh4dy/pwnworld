# Generated by Django 3.2.7 on 2021-09-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_users_chalssolvedname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='accountActive',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='challenges_solved',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]