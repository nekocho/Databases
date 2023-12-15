from lib.cohort import *

def test_construct_cohort():
    cohort = Cohort(1, 'cohort', '1-1-2023')
    assert cohort.id == 1
    assert cohort.cohort_name == 'cohort'
    assert cohort.starting_date == '1-1-2023'

def test_equal_cohort():
    cohort1 = Cohort(1, 'cohort', '1-1-2023')
    cohort2 = Cohort(1, 'cohort', '1-1-2023')
    assert cohort1 == cohort2

def test_format_cohort():
    cohort = Cohort(1, 'cohort', '1-1-2023')
    assert str(cohort) == "Cohort(1, cohort, 1-1-2023)"