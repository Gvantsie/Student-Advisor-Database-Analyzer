# Student-Advisor Database
This Python script, main.py, facilitates managing a student-advisor database using SQLite. It includes a class 
StudentAdvisorDatabase with methods for initializing the database, populating it with sample data, and executing 
various queries.

# Setup
Ensure you have Python installed on your system. You also need the sqlite3 module, which is part of Python's 
standard library.

# Usage
1) Setting up the Database:  
Initialize the database by creating an instance of the StudentAdvisorDatabase class, passing the database file 
name as an argument.

    > db = StudentAdvisorDatabase("Database.db")

2) Populating Sample Data:   
Before executing queries, populate the database with sample data using the populate_sample_data method.

    > db.populate_sample_data()

3) Querying the Database:   
Use the provided methods to query the database:

    - list_students(): Retrieves a list of all students.
    - list_advisors(): Retrieves a list of all advisors.
    - list_advisors_with_students(): Retrieves advisors along with the number of students each advises.
    - count_most_students_advisor(): Retrieves the advisor with the most students.
    - list_advisors_with_no_students(): Retrieves advisors with no students.

4) Closing the Connection:  
Ensure to close the database connection after executing queries.

    > db.close_connection()

# Notes
- Make sure you have the necessary permissions to read from and write to the specified database file.
- You can modify the populate_sample_data method to add more data or customize existing records directly in the database.
- You can modify the queries to suit your specific needs.
- This project has no specific requirements, but you can add more functionalities to the 'StudentAdvisorDatabase' class as needed.

> Gvantsa
