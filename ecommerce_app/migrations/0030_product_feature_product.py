# Generated by Django 3.2.4 on 2023-03-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0029_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature_product',
            field=models.BooleanField(default=False),
        ),
    ]