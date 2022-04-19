import sqlite3

conn = sqlite3.connect('details.db')

print ("Opened database successfully")

# cur = conn.cursor()
# cur.execute("SELECT * FROM events" );
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# cur.execute("SELECT * FROM events" );
# y=cur.fetchone()[0]
# print("Variable value is" +str(y));
# print(y);
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Display columns
print('\nColumns in EMPLOYEE table:')
data = cursor.execute('''SELECT * FROM  events''')
for column in data.description:
    print(column[0])


# # Display data
# print('\nData in EMPLOYEE table:')
# data=cursor.execute('''SELECT * FROM events''')
# for row in data:
#     print(row)


# print('\nData in column data:')
# data=cursor.execute('''SELECT data  FROM events''')
# for row in data:
#     print(row)

print('\nData in column data:')
data=cursor.execute("SELECT * FROM events WHERE data Like'I am going to define the test case as follows%'")
print(cursor.fetchall())
for row in data:
  print(row)