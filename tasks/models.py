import datetime
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('IN_REVIEW','IN_REVIEW'),
        ('APPROVED','APPROVED'),
        ('REJECTED','REJECTED'),
    ]
    description = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    completed_by = models.DateField(blank=True)
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='2', choices=STATUS_CHOICES)
    timestamp = models.DateField(default=datetime.datetime.now, blank=True)
    
    def __str__(self):
        return self.description
