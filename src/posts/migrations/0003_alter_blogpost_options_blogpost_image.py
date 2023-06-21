# Generated by Django 4.2.2 on 2023-06-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_blogpost_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_on'], 'verbose_name': 'Article'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
