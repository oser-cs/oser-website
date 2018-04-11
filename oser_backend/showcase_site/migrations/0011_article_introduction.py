# Generated by Django 2.0.3 on 2018-04-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_site', '0010_auto_20180411_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='introduction',
            field=models.TextField(blank=True, default='', help_text="Chapeau introductif qui sera affiché sous le titre de l'article. Utilisez-le pour résumer le contenu de l'article ou introduire le sujet."),
        ),
    ]
