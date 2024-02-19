import pytest
from main import Student

def test_enroll_students():
    students = Student()
    students.enrollStudents(5)
    assert students.getTotalStrength() ==  5

def test_drop_students():
    students = Student()
    students.enrollStudents(10)
    students.dropStudents(5)
    assert students.getTotalStrength() ==  5

def test_get_class_name():
    students = Student()
    assert students.getClassName() == 'Student'
