# Generated by Django 4.1.7 on 2023-03-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Registration',
        ),
    ]
