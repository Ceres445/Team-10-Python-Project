# Generated by Django 3.2.5 on 2021-08-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload', to='classes.assignment'),
        ),
    ]
