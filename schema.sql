drop table if exists users;
create table users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL
	);

drop table if exists trips;
create table trips (
	trip_id INTEGER PRIMARY KEY,
	trip_name TEXT NOT NULL,
	destination TEXT NOT NULL,
	friend TEXT NOT NULL,
	trip_user TEXT REFERENCES users(username)
	);

-- users and trips have many to many relationship
drop table if exists user_trips;
create table user_trips (
	id INTEGER PRIMARY KEY,
	user_id INTEGER,
	trip_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (trip_id) REFERENCES trips(trip_id)
	);
