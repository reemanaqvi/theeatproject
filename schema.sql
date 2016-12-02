drop table if exists users;
create table users (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
	street_address TEXT NOT NULL,
	city TEXT NOT NULL,
	state TEXT NOT NULL,
	zip INTEGER NOT NULL,
	password TEXT NOT NULL
	);

drop table if exists food;
create table food (
	food_id INTEGER PRIMARY KEY AUTOINCREMENT,
	food_name TEXT NOT NULL,
	ingredients TEXT NOT NULL,
	diet_restriction TEXT NOT NULL,
	cuisine_type TEXT NOT NULL,
	price INTEGER NOT NULL,
	phone_num INTEGER NOT NULL
	-- image BLOB NOT NULL
	);

-- users and foods have many to many relationship
drop table if exists user_foods;
create table user_foods (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user INTEGER,
	food INTEGER,
	FOREIGN KEY (user) REFERENCES users(user_id),
	FOREIGN KEY (food) REFERENCES foods(food_id)
	);
