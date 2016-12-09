from app import db
import sqlite3 as sql

def retrieve_user_foods(userid):
    query = []
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result_cur = cur.execute("select foodid from foods_user where userid =?",(userid,)).fetchall()
        for item in result_cur:
            print ("retrieving foods from retrieve foods")
            print (item[0])
        for item in result_cur:
            result = cur.execute("select * from food where id = ?",(item[0],)).fetchall()
            query.append(result[0])
    return query

def retrieve_food_markers():
    location = []
    food_ids = []
    info = []
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from food").fetchall()
        for item in result:
            location.append(food[street_address] + " " + food[city] + ", " + food[state] + " " + food[zip_code])
            food_ids.append(str(food[food_id]) + " " + food[food_name])
            info.append(zip(location, food_ids))
    return info

# def remove_food(id_value):
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         cur.execute("PRAGMA foreign_keys = ON")
#         result = cur.execute("delete from food where food_id=?",(id_value,))
#     return result

# def remove_food(id):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute('DELETE FROM food WHERE food_id = ?', (id,))
#         con.commit()
#         return True

def remove_food(id_value):
    print('removing foods')
    with sql.connect("app.db") as con:
        print("here")
        print(id_value)
        print(type('id_value'))
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute('DELETE FROM foods_user WHERE foodid=%s' % int(id_value))
        cur.execute('DELETE FROM food WHERE food_id=%s' % (int(id_value)))
        con.commit()
        return True

def retrieve_all_foods():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from food").fetchall()
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

def insert_food(food_name, ingredients, diet_restriction, cuisine_type, price, phone_num, user_id, lat, lng):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO food (food_name, ingredients, diet_restriction, cuisine_type, price, phone_num, lat, lng) VALUES (?,?,?,?,?,?,?,?)", (food_name, ingredients, diet_restriction, cuisine_type, price, phone_num, lat, lng))
        food_id = cur.lastrowid
        # cur.execute("INSERT INTO foods_user (userid,foodid) VALUES (?,?)", (user_id,food_id))
        cur.execute("INSERT INTO foods_user (userid, foodid) VALUES (?,?)", (user_id, food_id))
        # cur.execute("INSERT INTO users(username, password) VALUES (?,?)", ('HI', 'Parv'))
        con.commit()

def insert_user(username, password):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        con.commit()

def retrieve_foods(userid):
    query = []
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result_cur = cur.execute("select foodid from foods_user where userid =?",(userid,)).fetchall()
        for item in result_cur:
            result = cur.execute("select * from food where food_id = ?",(item[0],)).fetchall()
            query.append(result[0])
    print (query)
    return query
