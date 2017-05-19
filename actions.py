import psycopg2
import query

def display_mentors_name(connect):
    query.printing_query("""SELECT first_name, last_name FROM mentors;""", connect)

def display_nicknames(connect):
    query.printing_query("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", connect)

def carols_data(connect):
    query.printing_query("""SELECT concat(first_name, ' ', last_name),
        phone_number FROM applicants WHERE first_name='CAROL';""", connect)

def hat_owner(connect):
    query.printing_query("""SELECT concat(first_name ,' ', last_name), 
        phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""", connect)

def update_jemima(connect):
    query.modification_query("""UPDATE applicants SET phone_number='003670/223-7459'
        WHERE first_name='Jamima' and last_name='Foreman';""", connect)
    query.printing_query("""SELECT first_name, last_name, phone_number FROM applicants
        WHERE first_name='Jamima' and last_name='Foreman';""", connect)

def delete_arsenio_and_friend(connect):
    query.modification_query("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""", connect)