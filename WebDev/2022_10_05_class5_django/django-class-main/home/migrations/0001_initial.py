# Generated by Django 3.2.9 on 2022-10-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
