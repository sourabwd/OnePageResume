# Generated by Django 3.2.6 on 2021-08-07 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=200)),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='softwardata', to='resumeapp.professionalskills')),
            ],
        ),
        migrations.CreateModel(
            name='LanguagesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=200)),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='languagesdata', to='resumeapp.professionalskills')),
            ],
        ),
    ]