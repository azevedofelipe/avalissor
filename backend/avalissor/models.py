from django.db import models
from django.contrib.auth.models import User

class College(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


