# Generated by Django 2.0.2 on 2018-03-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitparticipant',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='accepté'),
        ),
    ]