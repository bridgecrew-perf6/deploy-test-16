# Generated by Django 3.2.9 on 2022-03-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_alter_status_contrag_alter_status_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='Done',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='ToDo',
            field=models.FloatField(null=True),
        ),
    ]
