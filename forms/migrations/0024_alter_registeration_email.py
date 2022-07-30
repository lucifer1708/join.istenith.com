# Generated by Django 4.0.6 on 2022-07-30 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0023_rename_social_links_insta_template_intro_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Kindly submit form with your college email only.', regex='^[2][1][a-z]{3}\\d{3}@[nith.ac.in]*')]),
        ),
    ]