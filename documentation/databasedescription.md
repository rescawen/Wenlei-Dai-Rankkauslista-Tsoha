# Database Description

Original database plans before starting the project.

##### User table

id | date_created | date_modified | username | password | ranking_points | wins | losses|

##### Tournament table 

id | date_created | date_modified | player_count | creator_id |

##### Match table

id | tournament_id | player1_id | player2_id 

##### Player -> Tournament table

player_id | tournament_id

##### Player -> Match table

player_id -> match_id 

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE tournament (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	player_count INTEGER NOT NULL, 
	description TEXT, 
	start_time DATETIME NOT NULL, 
	account_id INTEGER NOT NULL, 
	started BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	CHECK (started IN (0, 1))
)


CREATE TABLE players (
	account_id INTEGER NOT NULL, 
	tournament_id INTEGER NOT NULL, 
	PRIMARY KEY (account_id, tournament_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(tournament_id) REFERENCES tournament (id)
)


CREATE TABLE "match" (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	tournament_id INTEGER NOT NULL, 
	match_id INTEGER NOT NULL, 
	round_number INTEGER NOT NULL, 
	player1_id INTEGER, 
	player2_id INTEGER, 
	player1_name VARCHAR(144) NOT NULL, 
	player2_name VARCHAR(144) NOT NULL, 
	player1_score INTEGER NOT NULL, 
	player2_score INTEGER NOT NULL, 
	winner_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tournament_id) REFERENCES tournament (id), 
	FOREIGN KEY(player1_id) REFERENCES account (id), 
	FOREIGN KEY(player2_id) REFERENCES account (id), 
	FOREIGN KEY(winner_id) REFERENCES account (id)
)


