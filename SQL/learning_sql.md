## SQL syntax and language

# Creating databse

``````
psql -h 127.0.0.1 // enter psql
CREATE DATABASE music_library; // create a database

OR

createdb music_library // without entering psql
``````

# Importing seed to database

``````
psql -h 127.0.0.1 {database_name} < {file_containing_sql}  
``````

Make sure you are in directory the file is stored 

``````
SELECT * FROM artists; // pulls all information from artists table
``````

# Querying Data
``````
SELECT [columns to select] FROM [table name];
``````

Pulls information from specific table

``````
SELECT [columns to select] FROM [table name] WHERE [conditions];
``````

Filters information from specific table

We can use =, <, <=, >, >= to compare values.

Make sure to always use single quotes ('') to delimitate strings in conditions.

We can use the keywords AND and OR to combine conditions.


# Updating and Deleting Data

``````
UPDATE [table_name] SET [column_name] = [new_value];
``````
Updates the column with a new value from a specific table

``````
UPDATE [table_name] SET [column_name] = [new_value]
  WHERE [conditions];  
``````

Updates specific records with the conditions specified

``````
DELETE FROM [table_name] WHERE [conditions]; 
``````

# Creating New Data

```
INSERT INTO [table_name]
  ( [list of columns] )
  VALUES( [list of values] );
```

- In list of columns, can specify columns we need to insert values for 
- Best practice to specify all columns except id as this is updated automatically in psql


# Joining Multiple Tables

```
SELECT [columns to select]
  FROM [table name]
  JOIN [other table name]
  ON [join condition]

# Example:

SELECT albums.id, albums.title, artists.id, artists.name
  FROM albums // Left table
  JOIN artists // Right table
  ON artists.id = albums.artist_id; 
  
  // Make sure to prefix table name for specificity or error will occur
```

Combines rows from different tables 

For example, using the example below, you can combine album titles to artist name:

``````
SELECT albums.id,
      albums.title,
      artists.id,
      artists.name
  FROM albums
    JOIN artists
    ON artists.id = albums.artist_id;

``````

The code above gives:

```
 id |        title         | id |     name     
----+----------------------+----+--------------
  1 | Doolittle            |  1 | Pixies
  2 | Surfer Rosa          |  1 | Pixies
  3 | Waterloo             |  2 | ABBA
  4 | Super Trouper        |  2 | ABBA
  5 | Bossanova            |  1 | Pixies
  6 | Lover                |  3 | Taylor Swift
  7 | Folklore             |  3 | Taylor Swift
  8 | I Put a Spell on You |  4 | Nina Simone
  9 | Baltimore            |  4 | Nina Simone
 10 | Here Comes the Sun   |  4 | Nina Simone
 11 | Fodder on My Wings   |  4 | Nina Simone
 12 | Ring Ring            |  2 | ABBA

```

- As artist_id and album_id are both called 'id'
- Can use 'AS artist_id,' to artists.id to give it that alias.