# Generated by Django 2.2.dev20180517144303 on 2018-05-23 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('op_time', models.CharField(default='', max_length=30)),
                ('date', models.DateField(auto_now=True)),
                ('menu', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=30)),
                ('cafe_name', models.CharField(choices=[('SC', '학생식당'), ('PC', '교직원식당'), ('NPC', '신교직원식당'), ('NSC', '신학생식당'), ('D1', '제1 생활관'), ('D2', '제2 생활관'), ('HP', '행원파크')], max_length=30)),
            ],
        ),
    ]