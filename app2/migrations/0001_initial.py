# Generated by Django 3.2.3 on 2022-06-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=20)),
                ('userid', models.IntegerField()),
                ('salry', models.IntegerField()),
            ],
        ),
    ]