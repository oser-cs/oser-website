# Generated by Django 2.2 on 2021-01-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20201116_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]