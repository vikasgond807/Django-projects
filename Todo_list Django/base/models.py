from django.db import models
from pandas import describe_option
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) # Cascade deletes user data ! SET_NULL keeps the users data
    title=models.CharField(max_length=200)                                                                     # null means field can be empty ! blank-> 
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True) # takes automatic timestamp 

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']