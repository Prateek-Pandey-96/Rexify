# Generated by Django 3.1.4 on 2020-12-31 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutionName', models.CharField(max_length=100)),
                ('passingYear', models.CharField(max_length=5)),
                ('cityName', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SrSecondarySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutionName', models.CharField(max_length=100)),
                ('passingYear', models.CharField(max_length=5)),
                ('cityName', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=50)),
                ('proficiency', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SecondarySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutionName', models.CharField(max_length=100)),
                ('passingYear', models.CharField(max_length=5)),
                ('cityName', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('collegeInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.college')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.customer')),
                ('secondarySchoolInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.secondaryschool')),
                ('srSecondarySchoolInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.srsecondaryschool')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=50)),
                ('firmName', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('project1', models.CharField(max_length=100)),
                ('description1', models.TextField()),
                ('project2', models.CharField(max_length=100)),
                ('description2', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
            ],
        ),
    ]
