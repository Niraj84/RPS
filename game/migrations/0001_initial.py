# Generated by Django 3.1.7 on 2022-01-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('result', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]