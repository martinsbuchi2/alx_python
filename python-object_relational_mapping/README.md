# Python - Object-relational mapping

# Background Context and Objectives

Two major concepts: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy, an Object Relational Mapper (ORM).

Objectives include:

    * How to connect to a MySQL database from a Python script
    * How to SELECT rows in a MySQL table from a Python script
    * How to INSERT rows in a MySQL table from a Python script
    * What ORM means
    * How to map a Python Class to a MySQL table

# Tasks:

1. Write a script that lists all states from the database hbtn_0e_0_usa

2. Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

3. Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

4. Write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

5. Write a script that lists all cities from the database hbtn_0e_4_usa

6. Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

7. Write a python file that contains the class definition of a State and an instance Base = declarative_base()

8. Write a script that lists all State objects from the database hbtn_0e_6_usa

9. Write a script that prints the first State object from the database hbtn_0e_6_usa

10. Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa