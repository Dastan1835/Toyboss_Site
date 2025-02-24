# Generated by Django 5.1.2 on 2024-10-28 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toybos_products', '0020_aboutme_description_ky_aboutme_description_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='short_description_kz',
            new_name='short_description_kk',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ingredients_kz',
            new_name='ingredients_kk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='short_description_kz',
            new_name='short_description_kk',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='recipes',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='recipes',
            old_name='directions_kz',
            new_name='directions_kk',
        ),
        migrations.RenameField(
            model_name='recipes',
            old_name='ingredients_kz',
            new_name='ingredients_kk',
        ),
        migrations.RenameField(
            model_name='recipes',
            old_name='title_kz',
            new_name='title_kk',
        ),
    ]
