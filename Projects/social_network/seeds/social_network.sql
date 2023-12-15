DROP TABLE IF EXISTS user_accounts cascade;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;
DROP TABLE IF EXISTS posts cascade;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
-- The foreign key name is always {other_table_singular}_id
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);


INSERT INTO user_accounts (email_address, username) VALUES ('bobby@ymail.com', 'bobasaurus');
INSERT INTO user_accounts (email_address, username) VALUES ('cassie@boxmail.com', 'cassiethesloth');
INSERT INTO user_accounts (email_address, username) VALUES ('lizzierocks@rmail.com', 'lizzierocks');

INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Life', 'Its been a rollercoaster', 5, 3);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Happy birthday!', 'Turning 29 today', 200, 1);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Sloths', 'I really like sloths', 1, 2);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Promotion!', 'I got a promotion at work today!', 30, 3);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Zoo', 'I saw my favourite animal today', 60, 2);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('Guitars', 'Bought a new guitar today', 150, 1);