# Generated by Django 4.1.3 on 2022-12-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='fjkjk', upload_to='pics'),
            preserve_default=False,
        ),
    ]