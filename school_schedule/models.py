from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва предмету")
    description = models.TextField(blank=True, verbose_name="Опис")
    credits = models.IntegerField(default=1, verbose_name="Кількість годин на тиждень")  # нове поле
    is_core = models.BooleanField(default=True, verbose_name="Основний предмет")  # нове поле

    def __str__(self):
        return self.name


class SchoolClass(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Назва класу")
    year = models.IntegerField(verbose_name="Рік навчання")
    homeroom_teacher = models.ForeignKey('Teacher', null=True, blank=True, on_delete=models.SET_NULL,
                                         verbose_name="Класний керівник")  # нове поле
    number_of_students = models.IntegerField(default=0, verbose_name="Кількість учнів")  # нове поле

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    experience_years = models.IntegerField(default=0, verbose_name="Років стажу")  # нове поле
    email = models.EmailField(blank=True, verbose_name="Email")  # нове поле

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name="Клас")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")  # нове поле
    address = models.CharField(max_length=200, blank=True, verbose_name="Адреса")  # нове поле

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    classroom = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name="Клас")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Вчитель")
    day_of_week = models.CharField(max_length=20, verbose_name="День тижня")
    time = models.TimeField(verbose_name="Час початку")
    room_number = models.CharField(max_length=10, blank=True, verbose_name="Номер аудиторії")  # нове поле
    duration_minutes = models.IntegerField(default=45, verbose_name="Тривалість заняття")  # нове поле

    def __str__(self):
        return f"{self.day_of_week} {self.time} - {self.subject}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Учень")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    grade = models.IntegerField(verbose_name="Оцінка")
    date = models.DateField(verbose_name="Дата")
    comment = models.TextField(blank=True, verbose_name="Коментар вчителя")  # нове поле
    is_final = models.BooleanField(default=False, verbose_name="Підсумкова оцінка")  # нове поле

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"