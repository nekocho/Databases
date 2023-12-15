-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipe;
DROP SEQUENCE IF EXISTS recipe_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipe_id_seq;
CREATE TABLE recipe (
  id SERIAL PRIMARY KEY,
  recipe_name text,
  average_cooking_time int,
  rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipe (recipe_name, average_cooking_time, rating) VALUES ('Curry Chicken', 30, 4);
INSERT INTO recipe (recipe_name, average_cooking_time, rating) VALUES ('Tonkotsu Ramen', 15, 5);
INSERT INTO recipe (recipe_name, average_cooking_time, rating) VALUES ('Sushi', 20, 5);
INSERT INTO recipe (recipe_name, average_cooking_time, rating) VALUES ('Instant Noodles', 5, 2);

