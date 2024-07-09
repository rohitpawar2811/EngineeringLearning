## Databases

Mysql: 

1. Schema
2. Database
3. Client
4. Server

Connect Mysql

Database: Storing
DBMS: Database Management System 
- Manging the database

# Types of databases:

1. RDBMS
    - Genrally used for relational data
    - Fast transaction time,
    - Data consistency
    - ACID and transactional db.


2. NOSQL
    - Bulk unstructured data.
    - Fast processing data in bulk.


# ACID Properites, Normalization, types of relations in databases

DDL: create, db,table
DML: insert 
DQL(Data Query language): select 
DTL(Data transaction language): roolback and commit like things.

## Commands: 
1. drop database;
2. use db;
3. Create database db_name;
4. Create table if not Exists employee
   (
	id INTEGER,
	employee_name Varchar(20)

    );
5. show tables;

6. show create table table_name 
//It will provide the the defination of table, I mean create statement.

7. Fixed column order, and all columns has to provide some value
	:Insert into employee values(1, "Rohit Pawar", 1000, "Date");
   
8. simply you can mention the column name 
Insert into employee (col1, col2, col3) values("1","Rohit Pawar", "2021-20-28")

9. Inserting multiple data in the cmds.

insert into empl (col1, col2, col3) values(3, "Amit","2023") () ();

10. Select * from employee_v1;

11. limit, group by , order by ASD, 

# Concepts:

Transactional databases are generaally meant for there data consistency 
How they would manage the consistence ACID Properties 

- By not let user to insert the garbage data we define some rule and restriction on the columns, so that system integrity manged thats we called Integrity constraints.

1. Integrity Constraints: garbage data, If some data doesn't follow the rules of insertion that data we called as garbage data. 

Constraints: some rules.

Integrity: The way we want it to be consitent, simply not let user to insert any grabage data.


1. By using the datatypes you would stop garbage value insertion in the databases. 

2. Sql Constraints 
They are used to specify rules for the data in tables

Constrains are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any voilation between the constraints and the data action, the action is aborated.

Example : 

1. NOT Null, - Values not null

2. Default , - has some default if provide null values or not inserted any values.

3. Unique, : Insures all values in the column must be diffrent. But allow 1 null as well

4. Primary Key, - Combination of Not Null + Unique. uniquely identifies each row in table. Thats why it can be null uniquely identify.

5. Foreign Key, - Prevent actions that would destroy links betwene tables.

6. CHECK - Ensures that a value in a column follows certains condition created by Check.


**Note Important**
- Mysql : In case of Unique constraints. It will allow multiple null value insertion. As mysql treat null values as infinite values which doesn't have any value. Thats why on each insertion null value treated as unique.
 Multple null value allows in case of Unique constaints. 

- Oracle : Only allow 1 null values in case of unique, As it has fixed value or size.

- Constraint_Name = Provide constraint names as if not provide then it will assume it default and assign something random name convention and problem encountered when we wanted to alter that constraint.
And Debugging is easy when we got any type of failure.

-------------------------------------------------------
# Defining custom contraint names:

Create table if not exits empl_with_constrainsts
(
    id Integer,
    name varchar(50) NOT NULL,
    salary Double,
    hiring_date Date Default '',
    Constraint unique_emp_id Unique (id),
    Constraint salary_check Check(salary > 1000)
);

-------------------------------------------------------

