# Generated by Django 4.2rc1 on 2023-03-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]