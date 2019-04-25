# Database Description

### CREATE TABLE statements when creating databases

CREATE TABLE account ( <br/>
	id INTEGER NOT NULL, <br/>
	date_created DATETIME, <br/>
	date_modified DATETIME, <br/>
	name VARCHAR(144) NOT NULL, <br/>
	username VARCHAR(144) NOT NULL, <br/>
	password VARCHAR(144) NOT NULL, <br/>
	PRIMARY KEY (id)<br/>
)

CREATE TABLE tournament (<br/>
	id INTEGER NOT NULL, <br/>
	date_created DATETIME, <br/>
	date_modified DATETIME, <br/>
	name VARCHAR(144) NOT NULL, <br/>
	player_count INTEGER NOT NULL, <br/>
	description TEXT, <br/>
	account_id INTEGER NOT NULL, <br/>
	started BOOLEAN NOT NULL, <br/>
	PRIMARY KEY (id), <br/>
	FOREIGN KEY(account_id) REFERENCES account (id), <br/>
	CHECK (started IN (0, 1))<br/>
)


CREATE TABLE players (<br/>
	account_id INTEGER NOT NULL, <br/>
	tournament_id INTEGER NOT NULL, <br/>
	PRIMARY KEY (account_id, tournament_id), <br/>
	FOREIGN KEY(account_id) REFERENCES account (id), <br/>
	FOREIGN KEY(tournament_id) REFERENCES tournament (id)<br/>
)


CREATE TABLE "match" (<br/>
	id INTEGER NOT NULL, <br/>
	date_created DATETIME, <br/>
	date_modified DATETIME, <br/>
	tournament_id INTEGER NOT NULL, <br/>
	match_id INTEGER NOT NULL, <br/>
	round_number INTEGER NOT NULL, <br/>
	player1_id INTEGER, <br/>
	player2_id INTEGER, <br/>
	player1_name VARCHAR(144) NOT NULL, <br/>
	player2_name VARCHAR(144) NOT NULL, <br/>
	player1_score INTEGER NOT NULL, <br/>
	player2_score INTEGER NOT NULL, <br/>
	winner_id INTEGER, <br/>
	PRIMARY KEY (id), <br/>
	FOREIGN KEY(tournament_id) REFERENCES tournament (id), <br/>
	FOREIGN KEY(player1_id) REFERENCES account (id), <br/>
	FOREIGN KEY(player2_id) REFERENCES account (id), <br/>
	FOREIGN KEY(winner_id) REFERENCES account (id)<br/>
)

### Original database plans before starting the project.

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

