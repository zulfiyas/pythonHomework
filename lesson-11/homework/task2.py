import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 1
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
''')

# Step 2
books_data = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]

cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books_data)

# Step 3
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

# Step 4
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
print("Dystopian Books:", cursor.fetchall())

# Step 5
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# Bonus Task
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

# Update Ratings
ratings = [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
]
cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", ratings)

# Advanced 
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print("Books sorted by Year_Published:", cursor.fetchall())

conn.commit()
conn.close()
