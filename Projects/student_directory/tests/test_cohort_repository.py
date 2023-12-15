from lib.cohort import *
from lib.cohort_repository import *
from lib.student import *

def test_get_all_cohorts(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.all()

    assert cohort == [
        Cohort(1, "Blue", '2023-01-10'),
        Cohort(2, 'Red',	'2023-01-11')
       
    ]

def test_find_cohort(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find(1)
    assert cohort == Cohort(1, "Blue", '2023-01-10')

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohorts = repository.find_with_students(1)
    assert cohorts == Cohort(1, "Blue", '2023-01-10', [
        Student(1, 'Nathan', 1),
        Student(2, 'Emma', 1),
        Student(5, 'James', 1)
    ])


#Test create function

def test_create_cohort(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    repository.create(Cohort(3, 'Green', '2023-01-12'))

    result = repository.all()
    assert result == [
        Cohort(1, "Blue", '2023-01-10'),
        Cohort(2, "Red", '2023-01-11'),
        Cohort(3, 'Green', '2023-01-12')
    ]

#Test delete function

def test_delete_cohort(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    repository.delete(2)

    result = repository.all()
    assert result == [
        Cohort(1, "Blue", '2023-01-10')
    ]    