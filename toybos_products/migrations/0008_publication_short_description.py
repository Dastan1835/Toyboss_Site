# Generated by Django 5.1.2 on 2024-10-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toybos_products', '0007_publication_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='short_description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
