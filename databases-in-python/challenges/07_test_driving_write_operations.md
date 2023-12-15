# Test-driving write operations

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to test-drive "Repository" class methods to INSERT, DELETE and UPDATE.
### Designing a Repository class

We will build our repository class progressively over the next challenges. Here
is the previous table with new rows for `create` and `delete`:

| Method   | Job              | Arguments | SQL query it executes                                | Returns             |
| -------- | ---------------- | --------- | ---------------------------------------------------- | ------------------- |
| `all`    | Get all artists  | none      | `SELECT * FROM artists;`                             | A list of `Artist`s |
| `find`   | Get one artist   | `id`      | `SELECT * FROM artists WHERE id = $1;`               | A single `Artist`   |
| `create` | Insert an artist | `Artist`  | `INSERT INTO artists (name, genre) VALUES (%s, %s);` | Nothing             |
| `delete` | Delete an artist | `id`      | `DELETE FROM artists WHERE id = $1;`                 | Nothing             |

You can see an example of the code for these in the project starter.

## Demonstration

[Here's a video demonstration of test-driving the `create` and `delete`
methods.](https://www.youtube.com/watch?v=POF2BNCBAgI&t=3146s)

## Exercise

Your assignment is to test-drive a social network program. You should:

1. Set up a new project called `social_network` from the
   [starter](https://github.com/makersacademy/databases-in-python-project-starter).

2. Use the [Two Tables Design Recipe](../resources/two_table_design_recipe_template.md)
   to design and create a table for the following user stories:

   ```
   As a social network user,
   So I can have my information registered,
   I'd like to have a user account with my email address.

   As a social network user,
   So I can have my information registered,
   I'd like to have a user account with my username.

   As a social network user,
   So I can write on my timeline,
   I'd like to create posts associated with my user account.

   As a social network user,
   So I can write on my timeline,
   I'd like each of my posts to have a title and a content.

   As a social network user,
   So I can know who reads my posts,
   I'd like each of my posts to have a number of views.
   ```

3. Create a `seeds/social_network.sql`.
4. Test-drive the application to meet the user stories above.

[Example Solution](https://youtu.be/QLXyo8fuMOA&t=0s)

## Challenge

This is a process feedback challenge. That means you should record yourself doing it and
submit that recording to your coach for feedback. [How do I do
this?](https://github.com/makersacademy/golden-square/blob/main/pills/process_feedback_challenges.md)

Your assignment is to:

1. Test-drive a `create` method for your `AlbumRepository` class.
2. Test-drive a `delete` method for your `AlbumRepository` class.

Use your `music_library` project from the previous section.

[After you're done, submit your recording
here](https://airtable.com/shrvo9ePjlwnaiLv5?prefill_Item=dbpy_as03).


[Next Challenge](08_wrapping_in_application_class.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F07_test_driving_write_operations.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F07_test_driving_write_operations.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F07_test_driving_write_operations.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F07_test_driving_write_operations.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F07_test_driving_write_operations.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
