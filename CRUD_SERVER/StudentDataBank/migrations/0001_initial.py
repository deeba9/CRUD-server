# Generated by Django 4.2.7 on 2023-11-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=10)),
                ('cgpa', models.FloatField()),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
