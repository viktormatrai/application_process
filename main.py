from flask import Flask, render_template, request, redirect, url_for
import querys
from connect import open_database


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def diplsay_menu():
    return render_template("home.html")


@app.route('/mentors', methods=["GET", "POST"])
def mentors():
    cursor = open_database().cursor()
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors 
                        LEFT JOIN schools ON mentors.city = schools.city;""")
    rows = cursor.fetchall()
    return render_template("mentors.html", rows=rows)


@app.route('/all-school', methods=["GET", "POST"])
def all_school():
    cursor = open_database().cursor()
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors
                        RIGHT JOIN schools
                            ON mentors.city = schools.city;""")
    rows = cursor.fetchall()
    return render_template("all_school.html", rows=rows)


@app.route('/mentors-by-country', methods=["GET", "POST"])
def mentors_by_country():
    cursor = open_database().cursor()
    cursor.execute("""SELECT country, COUNT(mentors) FROM mentors
                        FULL JOIN schools
                            ON mentors.city = schools.city
                        GROUP BY country
                        ORDER BY country;""")
    rows = cursor.fetchall()
    return render_template("mentors_by_country.html", rows=rows)


@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    cursor = open_database().cursor()
    cursor.execute("""SELECT name, CONCAT(first_name, ' ', last_name) FROM mentors
                        INNER JOIN schools
                            ON mentors.id = schools.contact_person
                        ORDER BY name;""")
    rows = cursor.fetchall()
    return render_template("contacts.html", rows=rows)


@app.route('/applicants', methods=["GET", "POST"])
def applicants():
    cursor = open_database().cursor()
    cursor.execute("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                        FROM applicants
                        INNER JOIN applicants_mentors
                            ON applicants.id = applicants_mentors.applicant_id
                        WHERE applicants_mentors.creation_date > '2016/01/01'
                        ORDER BY applicants_mentors.creation_date DESC;""")
    rows = cursor.fetchall()
    return render_template("applicants.html", rows=rows)


@app.route('/applicants-and-mentors', methods=['GET', 'POST'])
def applicants_mentors():
    cursor = open_database().cursor()
    cursor.execute("""SELECT applicants.first_name, applicants.application_code, CONCAT(mentors.first_name, ' ', mentors.last_name)
                        FROM applicants
                        FULL JOIN applicants_mentors
                            ON applicants.id = applicants_mentors.applicant_id
                        LEFT JOIN mentors
                            ON applicants_mentors.mentor_id = mentors.id;""")
    rows = cursor.fetchall()
    return render_template('applicants_and_mentors.html', rows=rows)


if __name__ == '__main__':
    app.run()
