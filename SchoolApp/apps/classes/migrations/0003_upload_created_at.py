# Generated by Django 3.2.5 on 2021-08-11 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_upload_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]