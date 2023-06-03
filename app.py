from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# SQLite database configuration
DB_NAME = 'comments.db'

def create_comments_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments', methods=['POST'])
def add_comment():
    comment = request.form['comment']

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (comment) VALUES (?)', (comment,))
    conn.commit()
    conn.close()

    return 'Comment added successfully'

@app.route('/comments', methods=['GET'])
def get_comments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()
    conn.close()

    return {'comments': comments}

if __name__ == '__main__':
    create_comments_table()
    app.run()
