# Generated by Django 4.0.6 on 2022-07-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_alter_registeration_terms_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='terms_confirmed',
            field=models.BooleanField(db_column='Terms &Conditions', default=False),
        ),
    ]