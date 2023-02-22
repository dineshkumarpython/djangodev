# Generated by Django 3.2.4 on 2022-03-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DocterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Num',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Token', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230)),
                ('address', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('appointment_date', models.DateTimeField()),
                ('message', models.CharField(max_length=1100)),
                ('active', models.BooleanField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalapp2.departmentlist')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalapp2.docterlist')),
            ],
        ),
    ]