# Generated by Django 4.2.5 on 2023-10-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegie', '0002_vegie_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegie',
            name='recipe_image',
            field=models.ImageField(default='', upload_to='recipe/images/'),
        ),
    ]
