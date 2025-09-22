from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)  # Project title
    description = models.TextField()          # Project description
    technology = models.CharField(max_length=100)  # Technology used
    project_url = models.URLField(blank=True, null=True)  # Optional: Link to the project
    script_path = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.title
