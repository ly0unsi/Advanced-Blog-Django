# Generated by Django 3.1.4 on 2021-01-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0035_remove_settings_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sexe',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
