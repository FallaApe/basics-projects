import mysql.connector as myc

# connect to mysql database
con = myc.connect(host='localhost', user='root', passwd='password', database='movies')
cur = con.cursor()

def add_record(cur, con):
    # ask user for movie details
    title = input("Enter movie title: ")
    year = int(input("Enter release year: "))
    genre = input("Enter genre: ")
    rating = float(input("Enter rating: "))
    
    # insert new record into database
    cur.execute("INSERT INTO record (title, year, genre, rating) VALUES (%s, %s, %s, %s)", 
                (title, year, genre, rating))
    con.commit()
    con.close()
    print("Movie added successfully!")

def remove_record():
    # ask user for movie title to remove
    title1 = input("Enter the title of the movie to remove: ")
    cur = con.cursor()
    
    # delete record matching the given title
    cur.execute("DELETE FROM record WHERE title = %s", (title1,))
    if cur.rowcount > 0:
        print("Movie removed successfully!")
    else:
        print("Movie not found.")
    con.commit()
    con.close()

def view_records():
    # fetch and display all records from database
    cur = con.cursor()
    cur.execute("SELECT * FROM record")
    records = cur.fetchall()
    
    if records:
        print("\nMovies in the database:")
        for i in records:
            print(i)
    else:
        print("\nNo movies found in the database.")
    con.close()

def custom_query():
    # allow user to run any custom sql query
    cur = con.cursor()
    query = input("Enter your SQL query: ")
    cur.execute(query)
    
    # fetch and display results
    results = cur.fetchall()
    for row in results:
        print(row)
    
    con.commit()
    print("Query executed successfully.")
    con.close()

# main program loop
while True:
    print("\nOptions:")
    print("1. Add a record")
    print("2. Remove a record")
    print("3. View all records")
    print("4. Run a custom SQL query")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # reconnect to database before adding a record
        con = myc.connect(host='localhost', user='root', passwd='password', database='movies')
        cur = con.cursor()
        add_record(cur, con)
    elif choice == "2":
        remove_record()
    elif choice == "3":
        view_records()
    elif choice == "4":
        custom_query()
    elif choice == "5":
        # exit the program
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
