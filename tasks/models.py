from django.db import models


# Create your models here.
class Projects(models.Model):

    project_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=200)
    user_id = models.ForeignKey("users.users", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "projects"


class Tasks(models.Model):
    task_id = models.CharField(primary_key=True, max_length=50)
    name =  models.CharField(max_length=100)
    description = models.CharField(null=True, max_length=200)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    # Store 'H', 'M', or 'L' in the database (max_length=1 is enough)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )

    class Meta:
        db_table = "tasks"