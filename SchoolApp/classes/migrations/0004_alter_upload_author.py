# Generated by Django 3.2.5 on 2021-08-13 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0003_upload_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL),
        ),
    ]
