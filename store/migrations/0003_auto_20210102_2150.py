# Generated by Django 3.1.3 on 2021-01-02 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_productreview_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('E', 'Electronics'), ('S', 'Short'), ('OW', 'Fashion'), ('Bg', 'Bags'), ('Sh', 'Shoes'), ('SW', 'SportsWear'), ('F', 'Furniture')], max_length=2, null=True),
        ),
    ]
