import psycopg2
import connect


def show_mentors_name(connect):
    rows = connect.commands("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                FROM mentors
                                LEFT JOIN schools
                                    ON mentors.city = schools.city;""", connect)
    return rows


def show_all_schools_name(connect):
    rows = connect.commands("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                FROM mentors
                                RIGHT JOIN schools
                                    ON mentors.city = schools.city;""", connect)
    return rows


def count_mentors_by_country(connect):
    rows = connect.commands("""SELECT country, COUNT(mentors) FROM mentors
                                FULL JOIN schools
                                    ON mentors.city = schools.city
                                GROUP BY country
                                ORDER BY country;""", connect)
    return rows


def show_school_and_contact_person(conn):
    rows = connect.commands("""SELECT name, CONCAT(first_name, ' ', last_name) FROM mentors
                                INNER JOIN schools
                                    ON mentors.id = schools.contact_person
                                ORDER BY name;""", connect)
    return rows


def show_applicants_datas(conn):
    rows = connect.commands("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                                FROM applicants
                                INNER JOIN applicants_mentors
                                    ON applicants.id = applicants_mentors.applicant_id
                                WHERE applicants_mentors.creation_date > '2016/01/01'
                                ORDER BY applicants_mentors.creation_date DESC;""", connect)
    return rows


def show_applicants_and_mentors_datas(conn):
    rows = connect.commands("""SELECT applicants.first_name, applicants.application_code, CONCAT(mentors.first_name, ' ', mentors.last_name)
                                FROM applicants
                                FULL JOIN applicants_mentors
                                    ON applicants.id = applicants_mentors.applicant_id
                                LEFT JOIN mentors
                                    ON applicants_mentors.mentor_id = mentors.id;""", connect)
    return rows
