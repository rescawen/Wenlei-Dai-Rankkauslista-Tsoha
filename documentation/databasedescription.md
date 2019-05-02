# Database Description

### Database Normalization Clarification

There is only one place where it might seem that there are problems when it comes to redundant data. That is in the [player names columns](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/match/models.py#L19) of the match table. In reality it is just a [placeholder](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/match/models.py#L32) for a default value that is either `Player 1` and `Player 2` and we do not actually save the player names into it. 

When we query the list of matches in the views.py, we also query a separate the list of the players participating in the tournament. We then use the unique identifiers to [match](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/tour/views.py#L26) the name of the player from the players list to the player name in the match list. 

Having the attribute there makes it easy to do the matching and rendering placeholder `Player 1` and `Player 2`. It is also future proof, so that it ensures that in the scenario of the possibility of user being able to change their names, it would not affect the rendering of the tournament. 

### CREATE TABLE statements when creating databases

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


	CREATE TABLE match (
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

### Original database plans before starting the project.

One of the areas where I underestimated complexity is definitely the match table. It was supposed to be one of the simplest features, but turned out to be the single most difficult thing in the whole bracket, especially generating them. 

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

