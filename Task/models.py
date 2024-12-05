from django.db import models

# Create your models here. 

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_due = models.DateField()

    def __str__(self):
        return self.title
    
