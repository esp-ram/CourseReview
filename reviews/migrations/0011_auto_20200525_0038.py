# Generated by Django 3.0.6 on 2020-05-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_coursereview_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmessage',
            name='mensaje',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='coursereview',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
    ]
