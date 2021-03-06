# Generated by Django 2.1.5 on 2019-02-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=150)),
                ('event_address', models.CharField(max_length=300)),
                ('importance_rank', models.IntegerField()),
                ('event_description', models.CharField(max_length=300)),
            ],
        ),
    ]
