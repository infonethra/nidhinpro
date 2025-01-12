import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create and populate the database
def setup_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS version_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            version TEXT NOT NULL
        )
    """)
    # Insert sample data if table is empty
    cursor.execute("SELECT COUNT(*) FROM version_info")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO version_info (version) VALUES ('Python Version 3.10')")
        conn.commit()
    conn.close()

# Function to fetch the version from the database
def fetch_version():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT version FROM version_info LIMIT 1")
    version = cursor.fetchone()[0]
    conn.close()
    return version

# Function to handle button click
def show_version():
    version = fetch_version()
    messagebox.showinfo("Version Info", f"Version: {version}")

# Main application function
def main():
    # Setup the database
    setup_database()

    # Create GUI
    root = tk.Tk()
    root.title("Welcome to Python")
    root.geometry("300x200")

    # Welcome label
    label = tk.Label(root, text="Welcome to Python!", font=("Arial", 16))
    label.pack(pady=20)

    # Button to show version
    button = tk.Button(root, text="Show Version", command=show_version, font=("Arial", 12))
    button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
