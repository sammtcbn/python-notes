import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('student.db')

# Create a cursor
cursor = conn.cursor()

# Select all records from the table
cursor.execute("SELECT * FROM students")

# Fetch all records
records = cursor.fetchall()

# Print out each record
for record in records:
    print("Student ID:", record[0])
    print("Student Name:", record[1])
    print("Gender:", record[2])
    print()  # Add a blank line for readability

# Close the connection
conn.close()

