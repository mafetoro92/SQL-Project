import sqlite3


def creating_table():
    connection = sqlite3.connect('Colombia_universities.db')
    c = connection.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS Universities (
                          university_name TEXT,
                          location TEXT,
                          total_population INTEGER,
                          phone_number INTEGER,
                          email TEXT
                          )   """)

    connection.commit()
    connection.close()
