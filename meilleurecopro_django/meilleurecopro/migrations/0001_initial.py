# Generated by Django 5.2.4 on 2025-07-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('dept_code', models.CharField(max_length=200)),
                ('condominium_expenses', models.FloatField(max_length=200)),
                ('estate_url', models.CharField(max_length=200)),
            ],
        ),
    ]
