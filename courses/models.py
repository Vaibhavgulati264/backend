
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def _str_(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.IntegerField()
    semester = models.CharField(max_length=10)

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def _str_(self):
        return f"{self.course.title} - {self.year}-{self.semester}"