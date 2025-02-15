# Generated by Django 4.2.2 on 2023-12-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_activejobpostings_applicants_placements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='activejobpostings',
            name='application_deadline',
        ),
        migrations.RemoveField(
            model_name='activejobpostings',
            name='status',
        ),
        migrations.RemoveField(
            model_name='applicants',
            name='application_date',
        ),
        migrations.RemoveField(
            model_name='applicants',
            name='contact_information',
        ),
        migrations.RemoveField(
            model_name='placements',
            name='client_company',
        ),
        migrations.AddField(
            model_name='activejobpostings',
            name='experience_level',
            field=models.CharField(default='Skillset not specified', max_length=50),
        ),
        migrations.AddField(
            model_name='activejobpostings',
            name='required_skills',
            field=models.TextField(default='Skillset not specified'),
        ),
        migrations.AddField(
            model_name='activejobpostings',
            name='technology_stack',
            field=models.CharField(default='Python, Django', max_length=200),
        ),
        migrations.AddField(
            model_name='applicants',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='applicants',
            name='experience',
            field=models.TextField(default='No experience specified'),
        ),
        migrations.AddField(
            model_name='applicants',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='applicants',
            name='skills',
            field=models.TextField(default='No Skills specified'),
        ),
        migrations.AddField(
            model_name='placements',
            name='contract_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='activejobpostings',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='applied_job',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='placements',
            name='candidate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='placements',
            name='job_posting',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='placements',
            name='placement_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='placements',
            name='placement_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='placements',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklyinterviews',
            name='candidate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weeklyinterviews',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='weeklyinterviews',
            name='interview_outcome',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.RemoveField(
            model_name='weeklyinterviews',
            name='interviewers',
        ),
        migrations.AlterField(
            model_name='weeklyinterviews',
            name='job_posting',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='weeklyinterviews',
            name='interviewers',
            field=models.ManyToManyField(to='home.interviewer'),
        ),
    ]
