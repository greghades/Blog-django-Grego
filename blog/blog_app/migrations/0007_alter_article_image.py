# Generated by Django 4.1.1 on 2022-09-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='article/', verbose_name='Imagen'),
        ),
    ]
