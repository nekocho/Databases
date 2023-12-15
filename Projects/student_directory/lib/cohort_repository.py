from lib.cohort import *
from lib.student import *

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row['id'], row["cohort_name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM cohorts WHERE id = %s', [id])
        row = rows[0]
        return Cohort(row['id'], row["cohort_name"], row["starting_date"])
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            'SELECT cohorts.id as cohort_id, cohorts.cohort_name, cohorts.starting_date, students.id AS student_id, students.student_name ' \
            'FROM students ' \
            'JOIN cohorts '\
            'ON cohorts.id = students.cohort_id ' \
            'WHERE cohort_id = %s', [cohort_id]
        )
        students = []
        for row in rows:
            list = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(list)
        
        return Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'], students)

    

    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (id, cohort_name, starting_date) VALUES (%s, %s, %s)', [cohort.id, cohort.cohort_name, cohort.starting_date])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM cohorts WHERE id = %s', [id])
        return None