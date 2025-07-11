1.
import sqlite3

# Yangi baza yaratamiz (yoki mavjud bo‘lsa unga ulanadi)
conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()

# Roster jadvalini yaratamiz
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
conn.commit()

2.
# Ma'lumotlarni kiritamiz
members = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", members)
conn.commit()
3.
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()


4.
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()
print("Bajoran Members:")
for name, age in results:
    print(f"Name: {name}, Age: {age}")
