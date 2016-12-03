from app import db
import sqlite3 as sql

# def retrieve_foods(userid):
#     query = []
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         cur.execute("PRAGMA foreign_keys = ON")
#         result_cur = cur.execute("select tripid from trip_user where userid =?",(userid,)).fetchall()
#         for item in result_cur:
#             print "retrieving trips from retrieve trips"
#             print item[0]
#         for item in result_cur:
#             result = cur.execute("select * from trip where id = ?",(item[0],)).fetchall()
#             query.append(result[0])
#     return query

def remove_food(id_value):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("delete from food where food_id=?",(id_value,))
    return result

def retrieve_foods():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from foods").fetchall()
    return result

def retrieve_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select username from users").fetchall()
    return result

def authenticate(name, password):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from users where username = ? and password = ?", (name,password)).fetchall()
        print (result)
    return len(result) > 0

def retrieve_user_id(name):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select user_id from users where username = ?", (name,)).fetchall()
    return result

def insert_food(food_name,ingredients,diet_restriction, cuisine_type, price, phone_num, image, user_id):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO food (food_name, ingredients, diet_restriction, cuisine_type, price, phone_num, image) VALUES (?,?,?,?,?,?,?)", (food_name,ingredients,diet_restriction, cuisine_type, price, phone_num, image))
        food_id = cur.lastrowid
        cur.execute("INSERT INTO user_foods (food,user) VALUES (?,?)", (food_id,user_id))
        con.commit()

def insert_user(username, street_address, city, state, zip_code, password):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO users (username, street_address, city, state, zip_code, password) VALUES (?,?,?,?,?,?)", (username, street_address, city, state, zip_code, password))
        con.commit()
