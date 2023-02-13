# Assignment 3 : Altering the database

Write SQL scripts that:
a. modify the type of a column;
b. add / remove a column;
c. add / remove a DEFAULT constraint;
d. add / remove a primary key;
e. add / remove a candidate key;
f. add / remove a foreign key;
g. create / drop a table.

For each of the scripts above, write another one that reverts the operation. Place each script in a stored procedure. Use a simple, intuitive naming convention.

Create a new table that holds the current version of the database schema. Simplifying assumption: the version is an integer number.

Write a stored procedure that receives as a parameter a version number and brings the database to that version.
