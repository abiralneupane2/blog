# Generated by Django 4.2.5 on 2023-09-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
