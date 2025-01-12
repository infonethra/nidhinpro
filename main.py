import sqlite3
import random
from flask import Flask, render_template

app = Flask(__name__)

# Function to get a random word from the database
def get_random_word():
    # Connect to the SQLite database
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()

    # Fetch all words from the database
    cursor.execute('SELECT word FROM words')
    words = cursor.fetchall()

    # Close the connection
    conn.close()

    # Return a random word from the list of words
    return random.choice(words)[0] if words else None

@app.route('/')
def index():
    # Get a random word
    word = get_random_word()
    return render_template('index.html', word=word)

if __name__ == "__main__":
    app.run(debug=True)
