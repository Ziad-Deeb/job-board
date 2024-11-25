from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)  # Job title
    description = models.TextField()          # Job description
    company = models.CharField(max_length=255)  # Company name
    location = models.CharField(max_length=255)  # Job location
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salary
    posted_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    application_deadline = models.DateField()  # Deadline for applications
    creator = models.ForeignKey(User, on_delete=models.CASCADE) # Links to the user who created the job


    def __str__(self):
        return self.title
