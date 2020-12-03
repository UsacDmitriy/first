-- CREATE TABLE students (
-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER
-- );

-- CREATE TABLE employees (
-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER
-- );



-- CRUD - Create, Read, Update, Delete

-- Create

INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 23);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 19);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 18);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 21);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 23);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 19);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 18);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 21);

-- Read

-- SELECT * FROM employees;

-- SELECT  first_name FROM employees;
-- SELECT  first_name, last_name FROM employees;

-- SELECT  first_name, age FROM employees WHERE first_name = "Jack";
-- SELECT  first_name, age FROM employees WHERE first_name IS "Jack";
