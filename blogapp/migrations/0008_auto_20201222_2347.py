# Generated by Django 3.1.4 on 2020-12-22 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20201222_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
