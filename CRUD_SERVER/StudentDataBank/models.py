from django.db import models


# Create your models here.
class Student(models.Model):
    roll_number = models.CharField(max_length=10, primary_key=True)
    cgpa = models.FloatField()
    gender = models.BooleanField()
    semester = models.IntegerField(default=0)


class CustomUserManager(models.Manager):
    pass


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=15, default="default_username")
    password = models.CharField(max_length=25)
    # Use a custom manager with a different name
    custom_manager = CustomUserManager()

    # Add the manager to the model
    objects = models.Manager()  # The default manager (can use any name)
    custom_objects = CustomUserManager()  # Your custom manager

    def __str__(self):
        return self.username


class Score(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Score: {self.score} for User: {self.user.username}"
