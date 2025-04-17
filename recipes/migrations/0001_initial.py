# Generated by Django 5.2 on 2025-04-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredient_details', models.JSONField()),
                ('instructions', models.JSONField()),
                ('servings', models.IntegerField()),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('category', models.JSONField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
