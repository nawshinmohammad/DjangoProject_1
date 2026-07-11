from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Tasks(models.Model):
    status_options=[
        ("1","To Do"),
        ("2","Doing"),
        ("3","Done"),
    ]
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
    task_title = models.CharField(max_length=200)
    description = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True )
    status = models.CharField(max_length=1, choices=status_options,default="1")
    def __str__(self):
        return self.task_title
    