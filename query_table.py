import sqlite3

insert_university = """INSERT INTO Universities
                    (university_name, location, total_population, phone_number, email)
                    VALUES (?,?,?,?,?)"""

get_universities = "SELECT * FROM Universities"

get_universities_by_name = ("SELECT * FROM Universities WHERE university_name = ?", "name")

get_more_population_universities = """
SELECT * FROM Universities WHERE university_name = ?
ORDER BY total_population DESC LIMIT 1;
"""

student_menu = """

please choose one of these options:

1)Add a new university.
2)See all universities.
3)Find a university by name.
4)See which university have more population.

"""


def query_info_table():
    connection = sqlite3.connect('Colombia_universities.db')
    c = connection.cursor()
    while (user_input := input(student_menu)) != '5':
        print(user_input)

        if user_input == '1':
            university_name = input('Enter university name')
            location = input('Enter the city')
            total_population = int(input('Enter all population'))
            phone_number = int(input('Enter the phone number'))
            email = input('Enter the email')

            c.execute(insert_university, (university_name, location, total_population, phone_number, email))
            connection.commit()



        elif user_input == '2':
            c.execute(get_universities)
            items = c.fetchall()
            print(items)
            connection.commit()


        elif user_input == '3':
            name = input('Enter university name to find:')
            un = c.execute(get_universities_by_name, name )
            connection.commit()
            print(un)

        elif user_input == '4':
            name = input('Enter university name to find:')
            more_population = c.execute(get_more_population_universities, (name))
            print(f'The University with more population for {name}, is: {more_population}')

        else:
            print('Invalid input please try again')
