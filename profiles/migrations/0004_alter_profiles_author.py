# Generated by Django 4.2.7 on 2023-12-12 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('profiles', '0003_rename_aothor_profiles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
    ]