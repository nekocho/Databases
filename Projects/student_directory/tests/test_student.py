from lib.student import *

def test_construct_student():
    student = Student(1, 'Andy', 1)
    assert student.id == 1
    assert student.student_name == 'Andy'
    assert student.cohort_id == 1

def test_equal_student():
    student1 = Student(1, 'Andy', 1)
    student2 = Student(1, 'Andy', 1)
    assert student1 == student2

def test_format_student():
    student = Student(1, 'Andy', 1)
    assert str(student) == "Student(1, Andy, 1)"