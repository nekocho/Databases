# Single Table Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

students, names, cohorts
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| students              | student_name, cohort        |

Name of the table (always plural): `students`

Column names: `name`, `cohort`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
student_name: text
cohort: text
```

## 4. Write the SQL

```sql

-- file: student_directory.sql

-- Replace the table name, columm names and types.

CREATE TABLE student (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 student_directory_1 < student_table.sql
```

