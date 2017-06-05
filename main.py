from flask import Flask, render_template
import querys
import connect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('home_page.html')


if __name__ == "__main__":
    app.run()