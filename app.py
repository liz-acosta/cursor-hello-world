from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    pokemon = conn.execute('SELECT * FROM pokemon').fetchall()
    conn.close()
    return render_template('index.html', pokemon=pokemon)

@app.route('/pokemon/<int:id>')
def pokemon_profile(id):
    conn = get_db_connection()
    pokemon = conn.execute('SELECT * FROM pokemon WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('profile.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True) 