# Setting up PostgreSQL

Learn to set up PostgreSQL.

## Introduction

<!-- OMITTED -->

Up until now, you've been storing your program's data in memory — as attributes, lists, objects, etc. If we exit the program, all the data is lost, which is not great if we need to store data for the long term (think bank accounts, user accounts, order history...).

This week, you'll learn how to use a database to store data used by programs.

There are many types of databases, but this week you'll learn how to use **PostgreSQL**, which is a **relational database** software.

PostgreSQL is free and open-source, and is also widely used in a lot of large-scale, professional applications, which makes it the perfect choice for a first database to learn with.

## About relational databases

A **database** is a collection of **tables**. Each table stores a list of "things". For example, if our application is a blogging system, we could have a table 'posts' and a table 'comments'.

```
+----------------------------------------------------------+
|                                                          |
|   Database 'blog'                                        |
|                                                          |
|   +--------------------+       +--------------------+    |
|   |                    |       |                    |    |
|   |  Table 'posts'     |       |  Table 'comments'  |    |
|   |                    |       |                    |    |
|   +--------------------+       +--------------------+    |
+----------------------------------------------------------+
```

A table has **columns** for the attributes of the records, which are fixed and the same for each record (unless we're changing the schema of this table later). Each record is a **row** in the table.

For example, a table "students" could have columns "name" and "cohort_name".

Here's an example of how such a table would look like:

```
Table: students

 id |     name     | cohort_name
----+--------------+------------
  1 | Sarah        | April 2022
  2 | Georgia      | April 2022
  3 | David        | May 2022
  4 | Ali          | April 2022
```

*(By convention, table names and column names are **always lowercase**, using underscores to separate words). Table names are always plural.*

## Setup

First, you will need to install PostgreSQL on your machine. You can do this
using Homebrew on macOS. Here, we're using PostgreSQL 15 but if there's a newer
release you're asked to use, just substitute in that version number instead:

```bash
# Install postgresql.
$ brew install postgresql@15
```

Once installed, you'll need to make sure that installation directory is on your
`PATH` environment variable. In the output from the Homebrew installation you
just ran, should be a line which looks like this one:

```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
```

which you should copy, paste into the terminal and run.

Afterwards, either start a new terminal session or just run `zsh`.

<details>
  <summary>Why did we do that step? (optional details)</summary>

  We have just added a line to a file in our home directory, called `.zshrc`.
  The contents of this file are run whenever you start a new session, and you
  can force a new session to be used by typing `zsh`. Given this new line
  updates our `PATH` environment variable, we need that line to run before it
  can be used.
</details>

```bash
# Run this after the installation
# to start the postgresql software
# in the background.
$ brew services start postgresql@15

# You should get the following output:
==> Successfully started `postgresql@15` (label: homebrew.mxcl.postgresql@15)
```

If you have a different system, [follow the relevant instructions](https://www.postgresql.org/download/), and if you're not sure, ask your coach. If you have any trouble with the installation process, it's probably better to ask your coach for help, rather than spending too much time figuring it out.

## Demonstration

[Here's a video introduction and demonstration.](https://www.youtube.com/watch?v=9wT1FVQbPZw)


[Next Challenge](02_using_psql.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=sql_bites%2F01_setting_up_database.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=sql_bites%2F01_setting_up_database.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=sql_bites%2F01_setting_up_database.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=sql_bites%2F01_setting_up_database.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=sql_bites%2F01_setting_up_database.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
