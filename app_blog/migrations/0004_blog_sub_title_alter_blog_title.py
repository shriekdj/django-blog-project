# Generated by Django 4.0.1 on 2022-01-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sub_title',
            field=models.CharField(default='', max_length=264, verbose_name='Insert Sub-title'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Insert Title'),
        ),
    ]