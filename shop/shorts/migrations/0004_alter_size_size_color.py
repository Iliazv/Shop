# Generated by Django 4.0.1 on 2023-05-28 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0003_short_length_alter_short_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=25),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=40)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='shorts.short')),
            ],
        ),
    ]
