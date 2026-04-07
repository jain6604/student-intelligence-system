from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Student(models.Model):

    PROGRAM_CHOICES = [
        ('UG', 'Bachelors'),
        ('PG', 'Post Graduate'),
        ('LLB', 'LLB'),
        ('MBBS', 'MBBS'),
    ]

    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    program = models.CharField(max_length=10, choices=PROGRAM_CHOICES)
    year = models.IntegerField()
    semester = models.IntegerField(null=True, blank=True)  # not needed for MBBS

    def clean(self):
        # Bachelors (UG)
        if self.program == 'UG':
            if self.year > 4:
                raise ValidationError("Bachelors max year is 4")
            if self.semester and self.semester > 8:
                raise ValidationError("Bachelors max semester is 8")

        # Post Graduate (PG)
        elif self.program == 'PG':
            if self.year > 2:
                raise ValidationError("PG max year is 2")
            if self.semester and self.semester > 4:
                raise ValidationError("PG max semester is 4")

        # LLB
        elif self.program == 'LLB':
            if self.year > 5:
                raise ValidationError("LLB max year is 5")
            if self.semester and self.semester > 10:
                raise ValidationError("LLB max semester is 10")

        # MBBS
        elif self.program == 'MBBS':
            if self.semester:
                raise ValidationError("MBBS does not use semester")

    def __str__(self):
        return self.name


class Lifestyle(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    study_hours = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    sleep_hours = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    screen_time = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    attendance = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.student.name} Lifestyle"


class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cgpa = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    assignments_completed = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.student.name} Performance"