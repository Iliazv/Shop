# Generated by Django 4.0.1 on 2023-05-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0009_alter_comment_date_alter_comment_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.CharField(choices=[('5', 5), ('4', 4), ('3', 3), ('2', 2), ('1', 1)], default=0, max_length=10),
        ),
    ]
