# Generated by Django 2.0.6 on 2018-06-15 23:41

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_tutor_address'),
        ('dynamicforms', '0011_auto_20180616_0141'),
        ('projects', '0003_auto_20180615_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField(help_text="Les lycéens ne pourront plus s'inscrire après cette date.", verbose_name='date butoir')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicforms.Form', verbose_name='formulaire')),
                ('recipient', models.ForeignKey(blank=True, help_text='Tuteur/tutrice à qui envoyer les pièces justificatives. Son adresse doit être renseignée dans son profil.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Tutor', validators=[projects.models.validate_address_is_set], verbose_name='destinataire')),
            ],
            options={
                'verbose_name': 'formulaire projet',
                'verbose_name_plural': 'formulaires projet',
                'ordering': ('deadline',),
            },
        ),
    ]