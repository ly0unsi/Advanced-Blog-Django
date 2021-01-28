# Generated by Django 3.1.4 on 2021-01-01 18:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0029_auto_20201231_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('insragram', models.URLField(blank=True, null=True)),
                ('pinterest', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('About', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Social',
        ),
    ]
