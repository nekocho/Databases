# Test-driving a Repository class "find" method

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to test-drive a **Repository** class method to SELECT a single record from
the database.

## Intro

You previously learned how to test-drive a Repository class method to retrieve
_all_ records from a table (we named this method `all`).

In this section, you will learn how to test-drive a method `find` that returns
_a single record using its id_. It will perform a filtered `SELECT` query to
retrieve that single row.

### Designing a Repository class

We will build our repository class progressively over the next challenges. Here
is the previous table with a new row for `find`.

| Method | Job             | Arguments | SQL query it executes                  | Returns             |
| ------ | --------------- | --------- | -------------------------------------- | ------------------- |
| `all`  | Get all artists | none      | `SELECT * FROM artists;`               | A list of `Artist`s |
| `find` | Get one artist  | `id`      | `SELECT * FROM artists WHERE id = $1;` | A single `Artist`   |

You can see an example of the code for these in the project starter.

## Demonstration

[Here's a video demonstration of test-driving the `find`
method.](https://www.youtube.com/watch?v=POF2BNCBAgI&t=2528s)

## Exercise

Your assignment is to:

1. Test-drive a `find` method for your `AlbumRepository` class.
2. Modify `app.py` to print to the terminal the album with id 1 using your new
   `find` method.

Use your `music_library` project from the previous section.

[Example Solution](https://www.youtube.com/watch?v=POF2BNCBAgI&t=2931s)

## Challenge

Your assignment is to test-drive a recipe directory program. You should:

1. Set up a new project called `recipe_directory` from the
   [starter](https://github.com/makersacademy/databases-in-python-project-starter).
2. Use the [Single Table Design
   Recipe](../resources/single_table_design_recipe_template.md) to design and create a
   table for the following user stories:

   ```
   As a food lover,
   So I can stay organised and decide what to cook,
   I'd like to keep a list of all my recipes with their names.

   As a food lover,
   So I can stay organised and decide what to cook,
   I'd like to keep the average cooking time (in minutes) for each recipe.

   As a food lover,
   So I can stay organised and decide what to cook,
   I'd like to give a rating to each of the recipes (from 1 to 5).
   ```
  
3. Create a `seeds/recipes.sql` using `seeds/book_store.sql` as a template.
4. Test-drive a `Recipe` class that has attributes for each column in your
   table.
5. Test-drive a `RecipeRepository` class that has `all` and `find` methods.
6. Write a small program in `app.py` using the class `RecipeRepository` to print
   out the list of recipes to the terminal.


[Next Challenge](06_designing_schema_two_tables.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F05_test_driving_find_method.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F05_test_driving_find_method.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F05_test_driving_find_method.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F05_test_driving_find_method.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F05_test_driving_find_method.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
