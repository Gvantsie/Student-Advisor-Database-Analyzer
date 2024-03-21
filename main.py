import sqlite3


class StudentAdvisorDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        self.cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Advisor(
            AdvisorID INTEGER PRIMARY KEY,
            AdvisorName TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Student(
            StudentID INTEGER PRIMARY KEY,
            StudentName TEXT NOT NULL
        );


        CREATE TABLE IF NOT EXISTS Student_Advisor(
            StudentID INTEGER,
            AdvisorID INTEGER,
            FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
            FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
            PRIMARY KEY (StudentID, AdvisorID)
        );
        ''')
        self.conn.commit()

    def populate_sample_data(self):
        self.cursor.executescript('''
        INSERT OR IGNORE INTO Advisor(AdvisorID, AdvisorName) VALUES 
        (1,"Tsotne Sharvadze"), 
        (2,"Mariam Kiphsidze"), 
        (3,"John Smith"), 
        (4,"Sam Reeds"), 
        (5,"Arthur Clintwood");

        INSERT OR IGNORE INTO Student(StudentID, StudentName) VALUES 
        (101,"Gvantsa Euashvili"), 
        (102,"Nia Gergidze"), 
        (103,"Tinatin Tsakadze"), 
        (104,"Irakli Skhirtladze"), 
        (105,"Giga Samkharadze"), 
        (106,"Natia Phruidze"), 
        (107,"Gega kandelaki"), 
        (108,"Aleksandre kolbini"), 
        (109,"Nikoloz Kurdadze"), 
        (110,"Tornike Metreveli");

        INSERT OR IGNORE INTO Student_Advisor(StudentID, AdvisorID) VALUES
        (101, 1),
        (102, 1),
        (103, 3),
        (104, 2),
        (105, 4),
        (106, 2),
        (107, 2),
        (108, 3),
        (110, 1);
        ''')
        self.conn.commit()

    def list_advisors_with_students(self):
        self.cursor.execute('''
        SELECT a.AdvisorName, COUNT(sa.StudentID) AS Num_Students
        FROM Advisor a
        JOIN Student_Advisor sa ON a.AdvisorID = sa.AdvisorID
        GROUP BY a.AdvisorName
        ORDER BY a.AdvisorID
        ''')
        result = "List of Advisors with the Number of Students:\n"
        for row in self.cursor.fetchall():
            result += f"{row[0]} - {row[1]} students\n"
        return result

    def count_most_students_advisor(self):
        self.cursor.execute('''
        SELECT a.AdvisorName, COUNT(sa.StudentID) AS Num_Students
        FROM Advisor a
        JOIN Student_Advisor sa ON a.AdvisorID = sa.AdvisorID
        GROUP BY a.AdvisorName
        ORDER BY Num_Students DESC
        LIMIT 1
        ''')
        row = self.cursor.fetchone()
        return f"{row[0]} with {row[1]} students"

    def list_students(self):
        self.cursor.execute('''
        SELECT StudentName FROM Student
        ''')
        students = [row[0] for row in self.cursor.fetchall()]
        return students

    def list_advisors(self):
        self.cursor.execute('''
        SELECT AdvisorName FROM Advisor
        ''')
        advisors = [row[0] for row in self.cursor.fetchall()]
        return advisors

    def list_advisors_with_no_students(self):
        self.cursor.execute('''
        SELECT a.AdvisorName
        FROM Advisor a
        LEFT JOIN Student_Advisor sa ON a.AdvisorID = sa.AdvisorID
        WHERE sa.StudentID IS NULL
        ''')
        advisors = [row[0] for row in self.cursor.fetchall()]
        return advisors

    def close_connection(self):
        self.conn.close()


# check methods
db = StudentAdvisorDatabase("Database.db")
db.populate_sample_data()

print("Students:")
print(db.list_students())

print("\nAdvisors:")
print(db.list_advisors())

print("\nAdvisors with students:")
print(db.list_advisors_with_students())

print("\nAdvisor with the most students:")
print(db.count_most_students_advisor())

print("\nAdvisors with no students:")
print(db.list_advisors_with_no_students())

db.close_connection()
