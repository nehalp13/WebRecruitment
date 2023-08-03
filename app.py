# Install Flask and Flask-MySQLdb using pip:
# pip install Flask
# pip install Flask-MySQLdb

# app.py - Python Flask backend code

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations (modify these according to your MySQL setup)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'recruitment_db'

mysql = MySQL(app)

# Endpoint to receive and store job data from the front-end
@app.route('/post_job', methods=['POST'])
def post_job():
    data = request.json
    job_title = data['title']
    job_location = data['location']
    job_experience = data['experience']

    # Store the data in the MySQL database (you'll need to create the 'jobs' table)
    cur = mysql.connection.cursor()
    cur.execute(
        'INSERT INTO jobs (title, location, experience) VALUES (%s, %s, %s)',
        (job_title, job_location, job_experience)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Job posted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
