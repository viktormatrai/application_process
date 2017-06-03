import psycopg2

def connect_db():
    connect = psycopg2.connect("dbname='matraiv' user='matraiv' host='localhost' password='06pv24'")
    connect.autocommit = True           
    return connect

def commands(query, connect):
    cursor = connect.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
