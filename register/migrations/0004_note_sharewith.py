# Generated by Django 3.0.1 on 2020-07-19 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0003_remove_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='sharewith',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]