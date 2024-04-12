### Database SQL Samples
#### MPOP Reverse II
---
### Introduction
> This repository is just to share my knowledge about SQL
---
### Create a Databse
```SQL
CREATE DATABASE databasename;
```
> In the code above, it is just literally you want to create a database.
---
### Create a Table
```SQL
CREATE TABLE table_name (
	`column_name` `datatype` `length if possible`,
	...
)
```
> In this query, you may now create a simple table with columns and others, in creating a table, you've must know the required columns in a database, and the most important here is the ID. Belos is a sample query structure of a table.
```SQL
CREATE TABLE table_name (
	ID VARCHAR(20) NOT NULL PRIMARY KEY,
	firstname VARCHAR(20),
	middlename VARCHAR(20),
	lastname VARCHAR(20)
)
```
> In this sample query, you added that the ID is a required thing. The `NOT NULL` is the reason why it is required, also the `PRIMARY KEY` defines as unique, which means to say that it must not be copied of clone or duplicated.
---
### Creating a Data
```SQL
INSERT INTO table_name (ID, firstname, middlename, lastname) VALUES ('12345abcde', 'Juan', 'Apolo', 'Dela Cruz')
```
> In this query, you insert a data now in your table inside of your current database. If the data like first name exceed the limit you added for example is 12 in `VARCHAR(20)` it will going to cut it out or incomplete. In adding a data you don't need to fill up all the column name, or add all the column name, which is you only need to add is the required data which is the `ID` also the other related data which you want to add in.
---
### Reading a Data
```SQL
SELECT * FROM table_name
```
> So basically, this section of the program has the biggest part in the SQL. So maybe one of these days, I'm going to update it again. By the way, this query shows you all the data you inserted in your query, consider all the datas in the column. * means all columns. You may also specify the data you want to search like:

```SQL
SELECT * FROM table_name WHERE id = 1
```
> The result of this query is all the data that the table_name id is equivalent to 1. You may also use non primary key like names and others.

---
### Updating a Data
```SQL
UPDATE table_name SET column_name = 'data', ... WHERE ID = '12345abcde'
```
> In this query, you will going to update a specific data in your database, you may use the other conditional type like `LIKE` aside of using `=` in SQL. In addition, you may also use the [`WILDCARD`](#using-wildcards) since you're using `LIKE` keyword. **Take Note**, you need to add the `WHERE` and never forget, or else all the data from the selected columns will be changed. The `...` means and more, you may update some data in a column in one query, also a single column in a query.

---
### Deteting a Data
```SQL
DELETE FROM table_name WHERE ID = '12345abcde'
```
> The most sensitive part in SQL is the delete, if you forgot the condition `WHERE` all the data from your table will be deleted and can't be retrieve unless you hava e backup. In this query, you allowed to delete a data from a table name, not deleting a data in a single column.
---
### Using Wildcards
> Since this was mentioned on [Updating a Data](#updating-a-data), this is what wildcard is. We commonly use underscore (_) or percent (%) in doing a wildcard. Using of underscore is to search a data without knowing a character like Jo_n which returns to all data like John. The use of percent or modulo is if you don't know a bunch of characters like hello% which results to 'hello world', 'hello lord' and so on. The percent is based on what it is position or from zero to the moon, I mean, to where it goes. Below are just examples of SQL wildcards.

```SQL
SELECT * FROM table_name WHERE name LIKE '%Doe';
SELECT * FROM table_name WHERE name LIKE 'John%';
SELECT * FROM table_name WHERE name LIKE 'J%e';
SELECT * FROM table_name WHERE name LIKE 'J_hn _oe';
```

---
### About SQL
> Sometime, `INT` datatype won't work, so try to use `INTEGER` if ever you want to use `INTEGERS` as ID's datatype.
---
### Note
> This repository may not be frequently updated due to the schedules I have.