# Two Tables Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

students, cohorts, students names, cohorts names, cohorts starting dates, students cohorts
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| student               | student_name
| cohort                | cohort_name, starting_date

1. Name of the first table (always plural): `students` 

    Column names: `student_name`

2. Name of the second table (always plural): `cohorts` 

    Column names: `cohort_name`, `starting_date`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: students
id: SERIAL
student_name: text

Table: cohorts
id: SERIAL
cohort_name: text
starting_date: date
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one STUDENTS have many COHORTS? No
2. Can one COHORTS have many STUDENTS? Yes

You'll then be able to say that:

1. **Cohorts has many Students**
2. And on the other side, **Students belongs to Cohorts**
3. In that case, the foreign key is in the table Students

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one STUDENTS have many COHORTS? No
2. Can one COHORTS have many STUDENTS? Yes

1. **Cohorts has many Students**
2. And on the other side, **Students belongs to Cohorts**
3. In that case, the foreign key is in the table Students

```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date date,
);

-- Then the table with the foreign key second.

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int, 
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```

