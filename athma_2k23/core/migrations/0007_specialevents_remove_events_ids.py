# Generated by Django 4.2 on 2023-05-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_events_ids_alter_events_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(null=True)),
                ('eventdate', models.DateField(null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='events',
            name='ids',
        ),
    ]
