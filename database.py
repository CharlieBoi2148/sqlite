import sqlite3

# Connects to databse
conn = sqlite3.connect('home.db')

# Creates a cursor
c = conn.cursor()

# # Drops table
# c.execute("DROP TABLE homes")
# conn.commit()

# Creates a table
c.execute("""CREATE TABLE homes (
	address TEXT NOT NULL,
	region text,
	contact_info text

)
	""")
conn.commit()

# Add many records to a table
def add_many(list):
	conn = sqlite3.connect('home.db')
	c = conn.cursor()
	c.executemany("INSERT INTO homes VALUES (?,?,?)", (list))
	# Commit command and close connection
	conn.commit()
	conn.close()

# Shows all Records within a table 
def show_all():
	# Connect to database
	conn = sqlite3.connect('home.db')
	# Create a cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT rowid, * FROM homes")
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command
	conn.commit()
	# Close our connection
	conn.close()




print("command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()
