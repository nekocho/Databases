# Repository classes with many-to-many relationships

Learn to design Repository classes using many-to-many relationships.

## Intro

In this exercise, you will build on your `PostRepository` by adding a method
called `find_by_tag`, which will find all posts with a particular tag.

Here is how it should work:

```python
post_repository = PostRepository()

posts = post_repository.find_by_tag('coding')

# The array `posts` should contain the following Post objects:
#
#  * 1  How to use Git
#  * 2  Python classes
#  * 3  Using a Python REPL
#  * 7  SQL basics
```

| Method        | Job                              | Arguments      | SQL query          | Returns         |
| ------------- | -------------------------------- | -------------- | ------------------ | --------------- |
| `find_by_tag` | Find all posts for the given tag | A tag (string) | `SELECT ... JOIN ` | Array of `Post` |

<!-- OMITTED -->

## Exercise 

Set up a new project `blog` for this exercise.

Test-drive and implement Model and Repository classes for the table `posts`,
with the method `PostRepository#find_by_tag` having the behaviour described
above.

<!-- OMITTED -->

## Challenge

For this challenge, reuse the database schema created [in the previous
section](./03_using_joins_with_many_to_many.md) (with the Many-to-Many between
`posts` and `tags`).

Test-drive and implement Model and Repository classes for the table `tags`, with
the method `TagRepository#find_by_post`. This method should accept a post ID,
and return an array of related  `Tag` objects.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F05_repository_classes_many_to_many.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F05_repository_classes_many_to_many.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F05_repository_classes_many_to_many.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F05_repository_classes_many_to_many.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F05_repository_classes_many_to_many.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
