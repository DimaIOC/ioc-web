# Generated by Django 4.0.5 on 2022-07-03 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0028_subtypereporting_title_en_subtypereporting_title_uk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='subtypereporting',
        ),
    ]