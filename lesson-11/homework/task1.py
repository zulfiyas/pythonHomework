import sqlite3

# Step 1
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Roster")  # Ensuring a fresh start

cursor.execute("""
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

# Step 2
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

# Step 3
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# Step 4
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Step 5
cursor.execute("DELETE FROM Roster WHERE Age > 100")

# Step 6
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

rank_data = {
    "Benjamin Sisko": "Captain",
    "Ezri Dax": "Lieutenant",
    "Kira Nerys": "Major"
}

for name, rank in rank_data.items():
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))

# Step 7
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
sorted_roster = cursor.fetchall()
print("Sorted Roster:", sorted_roster)

# Commit changes and close connection
conn.commit()
conn.close()
