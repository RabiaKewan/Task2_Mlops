import pytest
from main import Student

def test_enroll_students():
    students = StudentsInMLOps()
    students.enrollStudents(7)
    assert students.getTotalStrength() ==  7

def test_drop_students():
    students = StudentsInMLOps()
    students.enrollStudents(200)
    students.dropStudents(100)
    assert students.getTotalStrength() ==  100

def test_get_class_name():
    students = StudentsInMLOps()
    assert students.getClassName() == 'Student'
