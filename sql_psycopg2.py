import psycopg2


# Connect to the "chinook" DB
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the DB
cursor = connection.cursor()

# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * from "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["test"])

# Query 4 - select only "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 from the "Albums" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', [
    "Queen"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
