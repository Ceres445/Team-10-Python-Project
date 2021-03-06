# Generated by Django 3.2.5 on 2021-08-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_remove_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=50)),
                ('permanent', models.BooleanField(default=True)),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('time', models.TimeField()),
                ('link', models.TextField(max_length=400)),
                ('key_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.classes')),
            ],
        ),
    ]
