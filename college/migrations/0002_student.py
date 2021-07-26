# Generated by Django 3.2.4 on 2021-07-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('act_composite', models.IntegerField()),
                ('act_english', models.IntegerField()),
                ('act_math', models.IntegerField()),
                ('sat_english', models.IntegerField()),
                ('sat_math', models.IntegerField()),
            ],
        ),
    ]