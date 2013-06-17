import sqlite3

from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    #create table
    c.execute("""CREATE TABLE ftasks(
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                due_date TEXT NOT NULL,
                priority INTEGER NOT NULL,
                status INTEGER NOT NULL)""")

    # insert dummy data into the table
    c.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES ("Finish this tutorial", "07/07/2013", 10, 1)')
    c.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES ("Finish my book", "07/07/2013", 10, 1)')

    name = "Learn JavaScript"
    due_date = "08/08/2013"
    priority = 1
    c.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES (?, ?, ?, 0)', [name, due_date, priority])
    c.close()

    # 1. we used a status of 1 to indicate that each of those tasks are considered "open" tasks
    # 2. we imported the DATABASE_PATH variable from the configuration file we created