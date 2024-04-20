# Generated by Django 4.1.7 on 2023-03-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_gallery_rename_contact_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='detail',
            field=models.TextField(),
        ),
    ]