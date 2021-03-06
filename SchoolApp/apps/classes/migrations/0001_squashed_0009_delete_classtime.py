# Generated by Django 3.2.6 on 2021-10-12 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('classes', '0001_initial'), ('classes', '0002_alter_upload_assignment'), ('classes', '0003_upload_created_at'), ('classes', '0004_alter_upload_author'), ('classes', '0005_alter_assignment_key_class'), ('classes', '0006_classinvitation'), ('classes', '0007_alter_classinvitation_email'), ('classes', '0008_classtime'), ('classes', '0009_delete_classtime')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_remove_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Title', max_length=400)),
                ('questions', models.FileField(blank=True, upload_to='questions/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ends_at', models.DateTimeField(blank=True, null=True)),
                ('key_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='home.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload', to='classes.assignment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ClassInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False, verbose_name='accepted')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='key')),
                ('sent', models.DateTimeField(null=True, verbose_name='sent')),
                ('email', models.EmailField(max_length=420, verbose_name='email_address')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('invited_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitees', to='home.classes')),
                ('inviter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
