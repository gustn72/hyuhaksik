# Generated by Django 2.0.5 on 2018-05-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyuhaksik', '0004_auto_20180525_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='univ_site',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('cafe_name', models.CharField(choices=[('SC', '학생식당'), ('PC', '교직원식당'), ('LR', '사랑방'), ('NPC', '신교직원식당'), ('NSC', '신학생식당'), ('D1', '제1 생활관'), ('D2', '제2 활관'), ('HP', '행원파크')], max_length=30)),
            ],
        ),
    ]
