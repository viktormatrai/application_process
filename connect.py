import psycopg2


def open_database():
    connect_data = psycopg2.connect("dbname='matraiv' user='matraiv' host='localhost' password='06pv24'")
    connect_data.autocommit = True
    return connect_data
