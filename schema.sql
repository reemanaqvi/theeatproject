drop table if exists users;
create table users (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
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
	phone_num INTEGER NOT NULL,
	-- street_address TEXT NOT NULL,
	-- city TEXT NOT NULL,
	-- state TEXT NOT NULL,
	-- zip_code INTEGER NOT NULL
	-- image BLOB NOT NULL
	lat REAL NOT NULL,
	lng REAL NOT NULL
	);

-- users and foods have many to many relationship
drop table if exists foods_user;
create table foods_user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	userid INTEGER,
	foodid INTEGER,
	FOREIGN KEY (userid) REFERENCES users(user_id),
	FOREIGN KEY (foodid) REFERENCES food(food_id) ON DELETE CASCADE
	);
