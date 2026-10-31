from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    joined_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = "users"
