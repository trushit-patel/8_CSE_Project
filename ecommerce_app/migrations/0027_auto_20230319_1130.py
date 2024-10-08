# Generated by Django 3.2.4 on 2023-03-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0026_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='logo',
            name='logo_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paymentpartners',
            name='url',
            field=models.CharField(default='trushitindus.pythonanywhere.com', max_length=255),
            preserve_default=False,
        ),
    ]
