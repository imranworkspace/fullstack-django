# Generated by Django 4.2.6 on 2023-11-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('s_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=150)),
                ('l_name', models.CharField(max_length=150)),
                ('stream', models.CharField(choices=[('bca', 'BCA'), ('mca', 'MCA')], max_length=150)),
            ],
        ),
    ]
