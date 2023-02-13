use [tennis-tournament];

CREATE TABLE Player(
	id int NOT NULL,
	name varchar(60) NOT NULL,
	age int,
	rank int,
	PRIMARY KEY(id)
);

ALTER TABLE Player
ADD points int;

ALTER TABLE Player
ADD country varchar(20);

ALTER TABLE Player 
ADD date_of_birth DATE;


CREATE TABLE Coach(
	id int NOT NULL,
	name varchar(60),
	player_id int,
	PRIMARY KEY(id),
	FOREIGN KEY(player_id)
		REFERENCES Player(id)
		ON DELETE CASCADE
);

ALTER TABLE Coach
ADD date_of_birth DATE;

ALTER TABLE Coach
DROP COLUMN date_of_birth;

ALTER TABLE Coach
ADD age INT;

ALTER TABLE Coach
ADD country varchar(40);

CREATE TABLE Tournament_type(
	id int NOT NULL,
	type_name varchar(30),
	points int,
	PRIMARY KEY(id)
);

CREATE TABLE Tournament(
	id int NOT NULL,
	name varchar(50) NOT NULL,
	country varchar(40) NOT NULL,
	PRIMARY KEY(id),
	tournament_type_id int,
	FOREIGN KEY(tournament_type_id)
		REFERENCES Tournament_type(id)
		ON DELETE CASCADE,
);

CREATE TABLE Playing_category(
	id int NOT NULL,
	category varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Tournament_playing_category(
	tournament_id int NOT NULL,
	playing_category_id int NOT NULL,
	FOREIGN KEY(tournament_id)
		REFERENCES Tournament(id)
		ON DELETE CASCADE,
	FOREIGN KEY(playing_category_id)
		REFERENCES Playing_category(id)
		ON DELETE CASCADE
);

CREATE TABLE Tournament_registration(
	player_id int NOT NULL,
	tournament_id int NOT NULL
	FOREIGN KEY(player_id)
		REFERENCES Player(id)
		ON DELETE CASCADE,
	FOREIGN KEY(tournament_id)
		REFERENCES Tournament(id)
		ON DELETE CASCADE
);

ALTER TABLE Tournament_registration
ADD CONSTRAINT PK_tr PRIMARY KEY(player_id, tournament_id)

ALTER TABLE Tournament_registration
DROP CONSTRAINT PK_tr

CREATE TABLE Fan(
	id int NOT NULL,
	name varchar(60) NOT NULL,
	age int,
	country varchar(40),
	PRIMARY KEY(id)
);

ALTER TABLE Fan
ADD nb_of_matches_attended int;

ALTER TABLE Fan 
ADD award varchar(10) DEFAULT NULL;

ALTER TABLE Fan
ALTER COLUMN award varchar(30);


CREATE TABLE Fanclub(
	id int NOT NULL,
	name varchar(40) NOT NULL,
	number_of_fans int,
	PRIMARY KEY(id)
);

CREATE TABLE Physiotherapists (
	id INT NOT NULL,
	name INT NOT NULL,
	player_id INT,
	FOREIGN KEY(player_id)
		REFERENCES Player(id),
	PRIMARY KEY (id, name)
);


SELECT name  
FROM sys.key_constraints  
WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = N'id';  
GO  

ALTER TABLE Fanclub
DROP CONSTRAINT ;


ALTER TABLE Fanclub
ADD CONSTRAINT PK_fc PRIMARY KEY (id, name);

ALTER TABLE Fanclub
ADD site_link varchar(50) DEFAULT NULL;



CREATE TABLE Fan_of_player(
	fan_id int NOT NULL,
	player_id int NOT NULL,
	fanclub_id int NOT NULL,
	FOREIGN KEY(fan_id)
		REFERENCES Fan(id)
		ON DELETE CASCADE,
	FOREIGN KEY(player_id)
		REFERENCES Player(id)
		ON DELETE CASCADE,
	FOREIGN KEY(fanclub_id)
		REFERENCES Fanclub(id)
);