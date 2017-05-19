import psycopg2

def display_menu():
    menu = input (""" 
            Press for the following actions:\n
            1 - display mentors name\n
            2 - display nickname of the mentors from Miskolc\n
            3 - Carols' full name & phone number\n
            4 - hat owners' full name & phone number\n
            5 - Mark Schaffarzyks' datas\n
            6 - update & display Jemima Foremans' phone number\n
            7 - delete Arsenio and his friend from the database\n
            0 - Quit
            """)
    return int(menu)

def connect_db():
    connect_str = "dbname='matraiv' user='matraiv' host='localhost' password='1989matraiv17'"
    connect = psycopg2.connect(connect_str)
    return connect

def printing_query(query, connect):
    cursor = connect.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def modification_query(query, connect):
    cursor = connect.cursor()
    cursor.execute(query)