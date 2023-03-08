import sqlite3

with sqlite3.connect('students.db') as con: 
    try: 
        con.execute("CREATE TABLE students (name TEXT, id TEXT, city TEXT)")
        print('database created')

    except Exception as e: 
        print(e)