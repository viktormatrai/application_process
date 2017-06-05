from flask import Flask, render_template
import querys
import connect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('home.html')


@app.route('/mentors', methods=['GET', 'POST'])
def mentors():
    connect = connect.connect_db()
    rows = querys.mentors()
    connect.close()
    return render_template('mentors.html', rows=rows)


@app.route('/all-school', methods=['GET', 'POST'])
def all_shool():
    connect = connect.connect_db()
    rows = querys.all_school(connect)
    conn.close()
    return render_template('al_school.html', rows=rows)


@app.route('/mentors-by-country', methods=['GET', 'POST'])
def mentors_by_country():
    connect = connect.connect_db()
    rows = querys.mentors_by_country(connect)
    connect.close()
    return render_template('mentors_by_country.html', rows=rows)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    connect = connect.connect_db()
    rows = query.contacts(conn)
    connect.close()
    return render_template('contacts.html', rows=rows)


@app.route('/applicants', methods=['GET', 'POST'])
def applicants():
    conn = connect.connect_db()
    rows = querys.applicants(connect)
    connect.close()
    return render_template('applicants.html', rows=rows)


@app.route('/applicants-and-mentors', methods=['GET', 'POST'])
def applicants_and_mentors():
    connect = connect.connect_db()
    rows = query.applicants_and_mentors(conn)
    conn.close()
    return render_template("applicants_and_mentors.html", rows=rows)


if __name__ == "__main__":
    app.run()
