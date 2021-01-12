# Generated by Django 3.1.3 on 2020-12-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201210_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='product_image',
            new_name='header_image',
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]