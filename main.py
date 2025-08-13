import django_setup
from school_schedule.models import Subject, Teacher, SchoolClass, Student, Grade, Schedule
from datetime import datetime

def add_subject():
    name = input("Назва предмету: ")
    description = input("Опис (необов'язково): ")
    Subject.objects.create(name=name, description=description)
    print(f"Предмет '{name}' додано!")

def add_teacher():
    first_name = input("Ім'я вчителя: ")
    last_name = input("Прізвище вчителя: ")
    subjects = Subject.objects.all()
    print("Доступні предмети:")
    for s in subjects:
        print(f"{s.id}: {s.name}")
    subject_id = int(input("ID предмету: "))
    subject = Subject.objects.get(id=subject_id)
    Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
    print(f"Вчитель {first_name} {last_name} доданий!")

def add_class():
    name = input("Назва класу: ")
    year = int(input("Рік навчання: "))
    SchoolClass.objects.create(name=name, year=year)
    print(f"Клас '{name}' додано!")

def add_student():
    first_name = input("Ім'я учня: ")
    last_name = input("Прізвище учня: ")
    classes = SchoolClass.objects.all()
    print("Доступні класи:")
    for c in classes:
        print(f"{c.id}: {c.name}")
    class_id = int(input("ID класу: "))
    school_class = SchoolClass.objects.get(id=class_id)
    Student.objects.create(first_name=first_name, last_name=last_name, school_class=school_class)
    print(f"Учень {first_name} {last_name} доданий!")

def add_schedule():
    day_of_week = input("День тижня: ")
    time_str = input("Час початку: ")
    time = datetime.strptime(time_str, "%H:%M").time()

    subjects = Subject.objects.all()
    print("Доступні предмети:")
    for s in subjects:
        print(f"{s.id}: {s.name}")
    subject_id = int(input("ID предмету: "))
    subject = Subject.objects.get(id=subject_id)

    classes = SchoolClass.objects.all()
    print("Доступні класи:")
    for c in classes:
        print(f"{c.id}: {c.name}")
    class_id = int(input("ID класу: "))
    classroom = SchoolClass.objects.get(id=class_id)

    teachers = Teacher.objects.filter(subject=subject)
    print("Доступні вчителі цього предмету:")
    for t in teachers:
        print(f"{t.id}: {t.first_name} {t.last_name}")
    teacher_id = int(input("ID вчителя: "))
    teacher = Teacher.objects.get(id=teacher_id)

    Schedule.objects.create(subject=subject, classroom=classroom, teacher=teacher,
                            day_of_week=day_of_week, time=time)
    print("Заняття додано!")

def add_grade():
    students = Student.objects.all()
    print("Доступні учні:")
    for s in students:
        print(f"{s.id}: {s.first_name} {s.last_name}")
    student_id = int(input("ID учня: "))
    student = Student.objects.get(id=student_id)

    subjects = Subject.objects.all()
    print("Доступні предмети:")
    for s in subjects:
        print(f"{s.id}: {s.name}")
    subject_id = int(input("ID предмету: "))
    subject = Subject.objects.get(id=subject_id)

    grade_value = int(input("Оцінка: "))
    date_str = input("Дата (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    comment = input("Коментар (необов'язково): ")

    Grade.objects.create(student=student, subject=subject, grade=grade_value, date=date, comment=comment)
    print("Оцінка додана!")