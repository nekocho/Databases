-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts cascade;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments cascade;
DROP SEQUENCE IF EXISTS comments_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);


CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  author_name text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, post_content) VALUES ('Title 1', 'Content 1');
INSERT INTO posts (title, post_content) VALUES ('Title 2', 'Content 2');
INSERT INTO posts (title, post_content) VALUES ('Title 3', 'Content 3');


INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 1', 'Jack', 1);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 2', 'Suzie', 3);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 3', 'Andy', 2);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 4', 'Barbara', 3);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 5', 'Emma', 2);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 6', 'Steven', 1);





