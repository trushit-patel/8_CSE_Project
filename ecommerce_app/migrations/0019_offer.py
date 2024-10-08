# Generated by Django 3.2.4 on 2023-03-09 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0018_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('expiration', models.DateTimeField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='ecommerce_app.product')),
            ],
        ),
    ]
