import psycopg2

def show_menu():
    menu = input (""" 
            Press for the following actions:
            1 - display mentors name\n
            2 - display nickname of the mentors from Miskolc\n
            3 - Carols' full name & phone number
            4 - hat owners' full name & phone number
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

def display_mentors_name(connect):
    printing_query("""SELECT first_name, last_name FROM mentors;""", connect)

def display_nicknames(connect):
    printing_query("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", connect)

def carols_data(connect):
    printing_query("""SELECT contact(first_name, ' ', last_name),
        phone_number FROM applicants WHERE first_name='CAROL';""", connect)

def hat_owner(connect):
    printing_query("""SELECT contact(first_name ,' ', last_name), 
        phone_number FROM applicants WHERE email like '%@adipiscingenimmi.edu';""", connect)

def update_jemima(connect):
    modification_query("""UPDATE applicants SET phone_number='003670/223-7459'
        WHERE first_name='Jamima' and last_name='Foreman';""", connect)
    printing_query("""SELECT first_name, last_name, phone_number FROM applicants
        WHERE first_name='Jamima' and last_name='Foreman';""", connect)

def delete_arsenio_and_friend(connect):
    modification_query("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""", connect)