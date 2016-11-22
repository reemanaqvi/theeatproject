import sqlite3 as sql

def insert_user(user_name, email):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, email) VALUES (?,?)", (user_name, email))
        customer_id = cur.lastrowid
        con.commit()

def insert_trip(trip_name, destination, friend, username):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("SELECT trip_id FROM trips WHERE trip_name = ? AND destination = ? AND friend = ? AND trip_user = ?", (trip_name, destination, friend, username))
        trip_id = cur.fetchone()
        if trip_id is None:
            cur.execute("INSERT INTO trips (trip_name, destination, friend, trip_user) VALUES (?,?,?,?)", (trip_name, destination, friend, username))
            trip_id = cur.lastrowid
        else:
            trip_id = trip_id[0]
        cur.execute("INSERT INTO user_trips (trip_id) VALUES (?)", (trip_id, ))
        con.commit()

def retrieve_users():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from users").fetchall()
    return result

def retrieve_friends():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        friends = cur.execute('SELECT * FROM users').fetchall()
        return friends

# def retrieve_trips():
#     # SQL statement to query database goes here
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("SELECT trips.trip_id, trip_name, destination FROM user_trips JOIN trips ON user_trips.id = trips.trip_id").fetchall()
#     return result

def retrieve_trips():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        trips = cur.execute("SELECT * from trips").fetchall()
    return trips

def delete_trip(id):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute('DELETE FROM trips WHERE trip_id = ?', (id,))
        con.commit()
        return True

def retrieve_trip_data(current_user):
    trips = []
    trip_rows = retrieve_trips()
    for trip_row in trip_rows:
        if trip_row['friend'] == current_user or trip_row['trip_user'] == current_user:
            trips.append(trip_row)
    return trips
