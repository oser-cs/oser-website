# Generated by Django 2.0.6 on 2018-06-15 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_editionform'),
    ]

    operations = [
        migrations.AddField(
            model_name='editionform',
            name='edition',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Edition', verbose_name='édition'),
        ),
        migrations.AlterField(
            model_name='editionform',
            name='form',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dynamicforms.Form', verbose_name='formulaire'),
        ),
    ]
