# Generated by Django 3.1.4 on 2021-01-09 14:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.0, message='you dont have enough budget to raise fund')])),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0, message='you should enter a valid amount')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.department')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('department', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'department')},
            },
        ),
    ]
