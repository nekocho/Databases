

-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS cohorts cascade;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students cascade;
DROP SEQUENCE IF EXISTS students_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) 
  references cohorts(id) 
  on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Blue', '2023-01-10');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Red',	'2023-01-11');


INSERT INTO students (student_name, cohort_id) VALUES ('Nathan',	1);
INSERT INTO students (student_name, cohort_id) VALUES ('Emma',	1);
INSERT INTO students (student_name, cohort_id) VALUES ('John',	2);
INSERT INTO students (student_name, cohort_id) VALUES ('Lizzie',	2);
INSERT INTO students (student_name, cohort_id) VALUES ('James',	1);
INSERT INTO students (student_name, cohort_id) VALUES ('Alesha',	2);


