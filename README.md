# udacity-fsnd-project1
Repository for Project 1 of the Full Stack Web Developer course

---

This project contains 2 files:

* project1.py: a python3 file which executes a series of queries against a database
* output.txt: a text file containing the printed output of project1.py

## Dependencies
The project1.py file has the following dependencies:

1. A PostgreSQL database named "news", as provided by Udacity for this course
2. python3
3. psycopg2

## Usage

If python3 is part of your PATH then you can execute project1.py directly from its containing directory via `./project1.py`.
Otherwise, you must invoke python3 at the command prompt, e.g. `python3 project1.py`

## Design

The project1.py file was designed as a single-use file. It leverages a method named QueryDb to fetch query results from the "news" PostgreSQL database. This method accepts a variable "query", which the remaning methods in the file pass into the QueryDb method. QueryDb instantiates a psycopg2 connection, creates a cursor, feeds the cursor's `execute` method the query, returns the result of the query via `cursor.fetchall()`, and closes both the cursor and connection.

The project1.py file executes 3 methods in a hard-coded order, with each method fetching query results from QueryDb and then formatting the results into printed statements.
