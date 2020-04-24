# Generated by Django 3.0.5 on 2020-04-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.FloatField()),
                ('words_per_minute', models.IntegerField()),
                ('characters_per_minute', models.IntegerField()),
                ('time', models.FloatField()),
            ],
        ),
    ]
