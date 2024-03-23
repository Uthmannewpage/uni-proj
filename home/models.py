from django.db import models

class ActiveJobPostings(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    technology_stack = models.CharField(max_length=200, default='Python, Django')
    required_skills = models.TextField(default='Skillset not specified')
    experience_level = models.CharField(max_length=50, default='Skillset not specified')

class Applicants(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    applied_job = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    skills = models.TextField(default='No Skills specified')
    experience = models.TextField(default='No experience specified')

class Interviewer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class WeeklyInterviews(models.Model):
    interview_date = models.DateField()
    interviewers = models.CharField(max_length=100,blank=True)
    candidate = models.CharField(max_length=100)
    job_posting = models.CharField(max_length=100)
    interview_outcome = models.CharField(max_length=100, default='Pending')
    comments = models.TextField(blank=True)

class Placements(models.Model):
    candidate = models.CharField(max_length=100)
    job_posting = models.CharField(max_length=100)
    placement_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    placement_status = models.CharField(max_length=50, default='Pending')
    contract_type = models.CharField(max_length=50, blank=True)
