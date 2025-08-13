from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва предмета')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Предмет"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SchoolClass(models.Model):
    name = models.CharField(max_length=10, verbose_name="Назва класу")


    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="students",
        verbose_name="Клас"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"