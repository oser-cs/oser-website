# Generated by Django 2.0.4 on 2018-04-29 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0003_auto_20180429_1053'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoringsession',
            name='tutoring_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='tutoring.TutoringGroup', verbose_name='groupe de tutorat'),
        ),
        migrations.AddField(
            model_name='tutortutoringgroup',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Tutor', verbose_name='Tuteur'),
        ),
        migrations.AddField(
            model_name='tutoringgroup',
            name='tutors',
            field=models.ManyToManyField(blank=True, related_name='tutoring_groups', through='tutoring.TutorTutoringGroup', to='profiles.Tutor', verbose_name='tuteurs'),
        ),
    ]
