# Generated by Django 2.2.2 on 2021-11-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menudata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=100)),
                ('menuingredients', models.CharField(max_length=100)),
            ],
        ),
    ]