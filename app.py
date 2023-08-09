from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'survey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('survey_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    question1 = request.form['question1']
    question2 = request.form['question2']

    # Store form data in MySQL database
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO survey_responses (name, lastname, email, question1, question2) VALUES (%s, %s, %s, %s, %s)",
        (name, lastname, email, question1, question2)
    )
    mysql.connection.commit()
    cursor.close()

    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port number here
