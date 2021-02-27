import sqlite3

def insert_records():

    many_universities = [
            ('Universidad El Rosario','Medellin', '8.450', '315-0987690', 'UniversidadElrosario@.com'),
            ('Universidad Javeriana','Bogota', '10.450', '315-0347654', 'Universidadjaveriana@.com'),
            ('Universidad Pontificia Bolivariana','Bucaramanga', '7.590', '320-0987654', 'UPB@.edu.com'),
            ('Universidad Minuto de Dios','Cali', '20.450', '311-0987654', 'Universidadminutodedios@.com'),
            ('Universidad de Antioquia','Medellin', '20.000', '350-0987654', 'UniversidaddeAntioquia@.com'),
            ('Universidad Nacional','Bogota', '30.450', '301-0987654', 'UniversidadNacional@.com'),
            ('Universidad Industrial de Santander','Bucaramanga', '11.450', '313-0987654', 'Universidadsantander@.com'),

        ]
    #connect to database
    connection = sqlite3.connect('Colombia_universities.db')
    # create a cursor
    c = connection.cursor()
    #create many records
    c.executemany("INSERT INTO Universities VALUES (?,?,?,?,?)", many_universities)

    connection.commit()
    connection.close()

