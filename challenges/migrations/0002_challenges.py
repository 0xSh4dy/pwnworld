# Generated by Django 3.2.7 on 2021-09-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challengeName', models.CharField(default='invalid', max_length=50)),
                ('flag', models.CharField(default='invalid', max_length=100)),
                ('solves', models.IntegerField(default=0)),
                ('difficultyLevel', models.CharField(max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
    ]
