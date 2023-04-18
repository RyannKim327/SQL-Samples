'### Database SQL Samples
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
> So basically, this section of the program has the biggest part in the SQL. So maybe one of these days, I'm going to update it again. By the way, this query shows you all the data you inserted in your query, consider all the datas in the column. * means all columns.

### Updating a Data
```SQL
```
>