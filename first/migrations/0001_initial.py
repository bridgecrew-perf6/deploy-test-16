# Generated by Django 4.0 on 2022-03-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.IntegerField()),
                ('v2', models.CharField(max_length=255)),
                ('v3', models.IntegerField()),
            ],
        ),
    ]
