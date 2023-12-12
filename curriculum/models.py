from django.db import models


# Create your models here.

class Job(models.Model):
    JOB_POSITION_CHOICES = [
        ('DevOps', 'DevOps'),
        ('Software Engineer', 'Software Engineer'),
        ('Project Manager', 'Project Manager'),
        ('SSr. ServiceNow Monitoring Integration', 'SSr. ServiceNow Monitoring Integration'),
        ('Jr. CEM Arch & Infrastructure Analyst', 'Jr. CEM Arch & Infrastructure Analyst'),
        ('Jr. CEM Operations', 'Jr. CEM Operatios'),
        ('Technical Solutions SSr.', 'Technical Solutions SSr.'),
        ('Tech Support & Customer Assistance', 'Tech Support & Customer Assistance'),
        
        # Add more choices as needed
    ]

    
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_position = models.CharField(max_length=200, choices=JOB_POSITION_CHOICES)
    job_description = models.TextField()
    job_tools = models.TextField()
    job_image = models.ImageField(upload_to='curriculum/media/curriculum', null=True, blank=True)
    job_salvame = models.TextField()

    def __str__(self):
        return self.job_title