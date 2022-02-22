# Generated by Django 3.2.9 on 2021-12-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishPhrases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=200, null=True)),
                ('uzbek', models.CharField(max_length=200, null=True)),
                ('example', models.TextField(max_length=300)),
            ],
        ),
    ]
