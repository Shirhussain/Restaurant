# Generated by Django 3.1 on 2020-10-22 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_auto_20201018_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'ordering': ['-created'], 'verbose_name': 'Meal', 'verbose_name_plural': 'Meals'},
        ),
        migrations.AddField(
            model_name='meals',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
