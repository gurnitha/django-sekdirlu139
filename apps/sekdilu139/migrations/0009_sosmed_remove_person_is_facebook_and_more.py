# Generated by Django 4.1.5 on 2023-01-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekdilu139', '0008_remove_person_sosmed_person_is_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sosmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_facebook',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_instagram',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_linkend',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_twitter',
        ),
        migrations.RemoveField(
            model_name='person',
            name='status',
        ),
        migrations.AddField(
            model_name='person',
            name='sosmed_id',
            field=models.ManyToManyField(to='sekdilu139.sosmed'),
        ),
    ]
