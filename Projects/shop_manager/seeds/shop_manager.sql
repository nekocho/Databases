-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS orders cascade;
DROP SEQUENCE IF EXISTS orders_id_seq;
DROP TABLE IF EXISTS items cascade;
DROP SEQUENCE IF EXISTS items_id_seq;

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  date text,
  customer_name text,
  item_name text
);

-- Then the table with the foreign key second.
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  item_name text,
  price int,
  item_amount int,
-- The foreign key name is always {other_table_singular}_id
  order_id int,
  constraint fk_order foreign key(order_id)
    references orders(id)
    on delete cascade
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO orders (date, customer_name, item_name) VALUES ('20-10-2023', 'John', 'Super Shark Vacuum Cleaner');
INSERT INTO orders (date, customer_name, item_name) VALUES ('10-09-2023', 'Bob', 'Makerspresso Coffee Machine');
INSERT INTO orders (date, customer_name, item_name) VALUES ('5-08-2023', 'Lizzie', 'Sunglasses');

INSERT INTO items (item_name, price, item_amount, order_id) VALUES ('Super Shark Vacuum Cleaner', 99, 30, 1);
INSERT INTO items (item_name, price, item_amount, order_id) VALUES ('Makerspresso Coffee Machine', 69, 15, 2);
INSERT INTO items (item_name, price, item_amount, order_id) VALUES ('Sunglasses', 25, 20, 3);

