class Cohort:
    def __init__(self, id, cohort_name, starting_date, students = None):
        self.id = id
        self.cohort_name = cohort_name
        self.starting_date = starting_date
        self.students = students or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Cohort({self.id}, {self.cohort_name}, {self.starting_date})"