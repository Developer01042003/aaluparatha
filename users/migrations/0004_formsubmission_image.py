# Generated by Django 4.2.1 on 2023-10-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_basemodel_cashback_formsubmission_cashback'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='image',
            field=models.ImageField(default=False, upload_to='proofs'),
        ),
    ]
