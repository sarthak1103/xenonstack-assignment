# Generated by Django 3.1.7 on 2021-04-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enrolledstudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_number', models.IntegerField(blank=True, null=True)),
                ('course', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]