# Generated by Django 3.0.3 on 2020-03-10 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_course_coursereview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursereview',
            name='pub_date',
        ),
    ]
