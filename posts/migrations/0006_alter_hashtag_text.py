# Generated by Django 4.0.4 on 2022-06-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_hashtag_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='text',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]