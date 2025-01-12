import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('words.db')
cursor = conn.cursor()

# Create the words table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY,
                    word TEXT NOT NULL)''')

# Insert sample words into the table
words = ['Athu', 'Angel', 'Nidhi']
cursor.executemany('INSERT INTO words (word) VALUES (?)', [(word,) for word in words])

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and words table created.")
