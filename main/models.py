from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_info',
        null=True,  # Allow NULL values
        blank=True  # Make field optional in forms
    )
    assignment_name = models.CharField(max_length=250)
    due_date = models.CharField(max_length=250)
    
    def __str__(self):
        if self.user:
            return f"{self.user.username}'s assignment: {self.assignment_name}"
        return f"Assignment: {self.assignment_name}"