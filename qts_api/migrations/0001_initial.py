# Generated by Django 3.1.2 on 2020-10-15 03:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ad_listing',
            fields=[
                ('ad_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ad_name', models.CharField(max_length=150)),
                ('ad_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('ad_status', models.CharField(choices=[('NEW', 'New'), ('UPD', 'updated'), ('OUT', 'outdated'), ('DEL', 'deleted')], default=('NEW', 'New'), max_length=3)),
                ('ad_duration', models.DurationField()),
                ('is_ad_promoted', models.BooleanField(default=False)),
                ('promotion_duration', models.DurationField()),
                ('ad_posted_date', models.DateField(default=datetime.date.today)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ad_type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
                ('Is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='parent_category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='promotion_package',
            fields=[
                ('promotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('promotion_name', models.CharField(max_length=150)),
                ('promotion_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('duration', models.DurationField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('address', models.TextField(default='')),
                ('contact', models.CharField(max_length=20)),
                ('user_type', models.CharField(default='new user', max_length=150)),
                ('json_token', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=120)),
                ('is_deleted', models.BooleanField(default=False)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.parent_category')),
            ],
        ),
        migrations.CreateModel(
            name='promoted_ad_detail',
            fields=[
                ('pa_ad_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('starting_date', models.DateField()),
                ('status', models.CharField(choices=[('NEW', 'New'), ('UPD', 'updated'), ('OUT', 'outdated'), ('DEL', 'deleted')], default='NEW', max_length=3)),
                ('is_deleted', models.BooleanField()),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.ad_listing')),
                ('promotion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.promotion_package')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField()),
                ('payment_time', models.TimeField()),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('payment_status', models.BooleanField(default=True)),
                ('promoted_ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.promoted_ad_detail')),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('image_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(default='')),
                ('is_deleted', models.BooleanField(default=False)),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.ad_listing')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(default=0)),
                ('comments', models.TextField(default='')),
                ('user_id', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('commented_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.user')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=70)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.district')),
            ],
        ),
        migrations.AddField(
            model_name='ad_listing',
            name='ad_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.sub_category'),
        ),
        migrations.AddField(
            model_name='ad_listing',
            name='ad_posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.user'),
        ),
        migrations.AddField(
            model_name='ad_listing',
            name='ad_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.ad_type'),
        ),
        migrations.AddField(
            model_name='ad_listing',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qts_api.city'),
        ),
    ]
