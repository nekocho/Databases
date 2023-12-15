# Creating a sequence diagram for a database-backed program

In this section, you will step away from the code for a bit and learn how to build sequence diagrams to communicate what how your program is working.

Why should you bother with this? 

As you've probably noticed, the number of files in your codebase has grown considerably compared to codebases you were working with in previous exercises. In real applications, codebases can easily contain hundreds or even thousands of files. No one can hold all that information in their head at once.

 * A diagram is easier to digest, present and discuss than a whole program made of written code. It is also easier to modify if it's needed.
 * It will force you to think deeper about what is happening in your program, and to explain to yourself (and your peers) how the different components of the app is working. This will become very useful when it comes to debugging too.

**A sequence diagram** for a database-backed program helps us to explain and communicate two important things:
 * The interaction between the different components of the program and the database
 * The order in which the different parts interact together

Here is an example:

```mermaid
sequenceDiagram
    participant T as Terminal
    participant P as Python program
    participant D as Postgres database
    Note left of T: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 
    T->>P: Runs program
    P->>D: SQL query
    D->>P: Query result data
    P->>T: Prints results to the terminal
```

On the sequence diagram above, we can see that:
 * the two main components of our system are the Python program and the database
 * the two interactions happening between them are the sending of SQL queries from the program to the database and the returning of query results from the database to the program
 * The SQL query is sent to the database by the program, and then the results are sent back by the database
 
> **Note** : the database and the terminal are technically not a parts of our program, but they are part of the broader "system" the program lives in - therefore it is still important to include them.


## Exercise

The diagram presented above presents what happens in database-backed program at a high level. We can "zoom in" as needed, to illustrate more low level details. Here is a template of a more detailed sequence diagram for the program that prints out albums that you wrote in the [previous step](./02_test_driving_model_repository_classes.md#exercise).
However, some important information has been left out.

Using the codebase for that exercise, fill in the gaps in this diagram.

```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program (in app.py)
    participant ar as ____ class <br /> (in lib/____.py)
    participant db_conn as ____ class in (in lib/____.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python ____`
    app->>db_conn: Opens connection to database by calling ____ method on ____
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls ____ method on ____
    ar->>db_conn: Sends SQL query by calling ____ method on ____
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns an ____ of ____, one for each row of the ____ table

    db_conn->>ar: Returns an ____ of ____, one for each row of the ____ table
    loop 
        ar->>ar: Loops through ____ and creates a ____ object for every row
    end
    ar->>app: Returns ____ of ____ objects
    app->>t: Prints list of ____ to terminal
```

<details>
    <summary><b>Solution</b></summary>

<!-- OMITTED -->

> If the diagram doesn't render well inside this box, click the "<->" button in top right corner to expand it.

```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program (app.py)
    participant ar as AlbumRepository class <br /> (in lib/album_repository.py)
    participant db_conn as DatabaseConnection class <br /> (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python app.py`
    app->>db_conn: Opens connection to database calling method `connect` on DatabaseConnection
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls method `all` on AlbumRepository
    ar->>db_conn: Sends SQL query by calling method `execute` on DatabaseConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the albums table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the albums table
    loop 
        ar->>ar: Loops through list and creates an Album object for every row
    end
    ar->>app: Returns list of Album objects
    app->>t: Prints list of albums to terminal
```

Note that the `Album` class does not appear in the top line of boxes in this diagram. 
That's because it's not really an _actor_ in a program. 
It's just a container to hold the data for each album.
</details>

## Diagramming

You can create these diagrams in the diagramming tool of your choice but a nice
one for creating sequence diagrams specifically is
[diagram.codes](https://playground.diagram.codes/d/sequence).

After starting diagram.codes, you'll see an example in the left-hand panel which
is what's used to automatically draw what's in the right-hand panel. You can
make your own aliases, arrows between them, etc. by changing the content on the
left.

<details>
  <summary>Want to see an example of diagram.codes syntax?</summary>

  This code produces the first diagram on this page.

  ```
  alias T="Terminal"
  alias P="Python program"
  alias D="Postgres database"
  
  T->P: "Runs program"
  P->D: "SQL query"
  D->P: "Query result data"
  P->T: "Prints results to the terminal"
  ```
</details>

Some alternatives:

* [Mermaid's Live Editor](https://mermaid.live/) which allows for drawing
  sequences (check its Sample Diagrams section)
* [Excalidraw](https://excalidraw.com) which allows for more freehand drawing

## Challenge

This is a process feedback challenge. That means you should record yourself doing it and
submit that recording to your coach for feedback. [How do I do
this?](https://github.com/makersacademy/golden-square/blob/main/pills/process_feedback_challenges.md)

> **Note**: For this challenge, record yourself as you talk through your finished diagram (there is no need to record yourself as you create the diagram). As part of your submission, please upload an image file with your diagram as well as your recording.

Create a similar sequence diagram to the one above for the book_store from the
previous challenge. Make sure your diagram includes all of the [challenge you completed
in the previous
section](./02_test_driving_model_repository_classes.md#challenge). Make sure
your diagram includes the following:

 * The terminal 
 * The main program (`app.py`)
 * The repository class
 * The database connection class
 * The database

[After you're done, submit your recording and diagram here](https://airtable.com/shrvo9ePjlwnaiLv5?prefill_Item=dbpy_as02_v2).


[Next Challenge](04_designing_schema_one_table.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F03_creating_sequence_diagrams.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F03_creating_sequence_diagrams.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F03_creating_sequence_diagrams.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F03_creating_sequence_diagrams.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F03_creating_sequence_diagrams.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
