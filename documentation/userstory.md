# User Story

### When user lands on front/index page unregistered/not logged in

- User can see a partial list of the latest tournaments. For each tournament there is its name and player count displayed.

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament 
            ORDER BY tournament.date_modified DESC
            LIMIT ? OFFSET ?
  
- User can see the current amount of players signed up for the tournament in the blue bubble pill right to the name (this is the same for the rest of the tournament lists).

      SELECT COUNT(*) 
            FROM account 
            LEFT JOIN players ON players.account_id = account.id 
            WHERE (players.tournament_id = ?)

- User can log in.

      SELECT account.id AS account_id, 
            account.date_created AS account_date_created, 
            account.date_modified AS account_date_modified, 
            account.name AS account_name, 
            account.username AS account_username, 
            account.password AS account_password 
            FROM account 
            WHERE account.username = ? AND account.password = ?
            LIMIT ? OFFSET ?

- User can click `Register as new user` in the navigation bar to go to new account registration page (link doesn't have SQL statement).

### When user is in account registration page

- User can fill out a form with name, username and password to register.

      INSERT INTO account (date_created, date_modified, name, username, password) 
            VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

### When user is logged in and is in any page

- User can click `Tournament bracket application` in the navigation bar to return index page.
- User can click `All tournaments` in the navigation bar to go to all tournaments page.
- User can click `Joined tournaments` in the navigation bar to go to joined tournaments page.
- User can click `Owned tournaments` in the navigation bar to go to owned tournaments page.
- User can click `Create new tournament` in the navigation bar to go to new tournament creation page.
- User can log out. <br/>
 (links don't have SQL statement).

### When user is logged into index page

- User can see a partial list of the latest tournaments.
  
      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament ORDER BY tournament.date_modified DESC
            LIMIT ? OFFSET ?
            
- User can see number of all the tournaments it has signed up for above the list below.

      SELECT COUNT(*) 
            FROM tournament 
            LEFT JOIN players ON players.tournament_id = tournament.id 
            WHERE (players.account_id = ?)


- User sees a list of all tournaments it has signed up for. 

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament 
            JOIN players ON tournament.id = players.tournament_id 
            WHERE players.account_id = ? 
            ORDER BY tournament.date_modified DESC
            LIMIT ? OFFSET ?

- User sees a list of all tournaments it has created and administrates. 

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament 
            WHERE tournament.account_id = ? 
            ORDER BY tournament.date_modified DESC
            LIMIT ? OFFSET ?

- User can click a tournament name to take them into a specific tournament page (link doesn't have SQL statement).

### When user is logged and in all tournaments page

- User sees a partial list of all tournaments. 

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament ORDER BY tournament.date_modified DESC
            LIMIT 'ITEMS-PER-PAGE' OFFSET 'PAGE-NUMBER-MINUS-ONE-TIMES-ITEMS-PER-PAGE'
           
- User can continue to browse the rest of all tournaments through pagination (the following is only done if conditions in the [documenation](https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/__init__.py#L502) are fulfilled).

      SELECT count(*) AS count_1 
            FROM (SELECT tournament.id AS tournament_id, tournament.date_created AS tournament_date_created,      
            tournament.date_modified AS tournament_date_modified, tournament.name AS tournament_name, tournament.player_count AS 
            tournament_player_count, tournament.account_id AS tournament_account_id, tournament.description AS 
            tournament_description, tournament.started AS tournament_started 
            FROM tournament) AS anon_1
      
- User can click a tournament name to take them into a specific tournament page (link doesn't have SQL statement).

### When user is logged and in joined tournaments page

- User sees a partial list of all tournaments it has signed up for.
  
      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament JOIN players ON tournament.id = players.tournament_id 
            WHERE players.account_id = ? ORDER BY tournament.date_modified DESC
            LIMIT 'ITEMS-PER-PAGE' OFFSET 'PAGE-NUMBER-MINUS-ONE-TIMES-ITEMS-PER-PAGE'
  
- User can continue to browse the rest of joined tournaments through pagination (the following is only done if conditions in the [documenation](https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/__init__.py#L502) are fulfilled).

      SELECT count(*) AS count_1 
            FROM (SELECT tournament.id AS tournament_id, tournament.date_created AS tournament_date_created,            
            tournament.date_modified AS tournament_date_modified, tournament.name AS tournament_name, tournament.player_count AS 
            tournament_player_count, tournament.account_id AS tournament_account_id, tournament.description AS 
            tournament_description, tournament.started AS tournament_started 
            FROM tournament JOIN players ON tournament.id = players.tournament_id 
            WHERE players.account_id = ?) AS anon_1

- User can click a tournament name to take them into a specific tournament page (link doesn't have SQL statement).

### When user is logged and in owned tournaments page

- User sees a partial list of all tournaments it has created and administrates. 

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name,
            tournament.player_count AS tournament_player_count,       
            tournament.account_id AS tournament_account_id,
            tournament.description AS tournament_description,
            tournament.started AS tournament_started 
            FROM tournament 
            WHERE tournament.account_id = ? ORDER BY tournament.date_modified DESC
            LIMIT 'ITEMS-PER-PAGE' OFFSET 'PAGE-NUMBER-MINUS-ONE-TIMES-ITEMS-PER-PAGE'


- User can continue to browse the rest of all tournaments through pagination (the following is only done if conditions in the [documenation](https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/__init__.py#L502) are fulfilled).

      SELECT count(*) AS count_1 
            FROM (SELECT tournament.id AS tournament_id, tournament.date_created AS tournament_date_created,            
            tournament.date_modified AS tournament_date_modified, tournament.name AS tournament_name, tournament.player_count AS 
            tournament_player_count, tournament.account_id AS tournament_account_id, tournament.description AS 
            tournament_description, tournament.started AS tournament_started 
            FROM tournament 
            WHERE tournament.account_id = ?) AS anon_1


- User can click a tournament name to take them into a specific tournament page (link doesn't have SQL statement).

### When user is logged in and in tournament creation page

- User can fill out a form with name, maximum player count and optional description to create a new tournament.

      INSERT INTO tournament (date_created, date_modified, name, player_count, account_id, description, started) 
            VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)


### When user is logged in and in a specific tournament that has not started

- User can see the tournament title.

      SELECT tournament.id AS tournament_id, 
            tournament.date_created AS tournament_date_created, 
            tournament.date_modified AS tournament_date_modified, 
            tournament.name AS tournament_name, 
            tournament.player_count AS tournament_player_count, 
            tournament.account_id AS tournament_account_id, 
            tournament.description AS tournament_description, 
            tournament.started AS tournament_started 
            FROM tournament 
            WHERE tournament.id = ?

- User can see list of players who have signed up for the tournament.

      SELECT * FROM account 
            LEFT JOIN players ON players.account_id = account.id 
            WHERE (players.tournament_id = ?)

- User can click the `Join tournament` button to join the specific tournament.
      
      INSERT INTO players (account_id, tournament_id) VALUES (?, ?)

- If user is the creator of the tournament, then the user can choose to start the tournament regardless of it not reaching maximum player count with a minimum of one player (will have multiple SQL statements because we generating all the matches).

      (Query ids of the players because we need to use the list this for insertion into matches later)
      
      SELECT account_id FROM players WHERE tournament_id = ?
      
      (After some processing with the match generating algorithm we do the following as many times as there are matches)
     
      INSERT INTO match (date_created, date_modified, tournament_id, match_id, round_number, 
      player1_id, player2_id, player1_name, player2_name, player1_score, player2_score) 
      VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?)

      (Finally we toggle the tournament into started state)
      
      UPDATE tournament SET date_modified=CURRENT_TIMESTAMP, started=? WHERE tournament.id = ?

- If user is the creator of the tournament, then user can click `edit tournament` button to go to tournament edit page (link doesn't have SQL statement).

### When user is logged in and in tournament editing page as creator of the tournament
- User can see the title of the tournament it is editing (query used for prepopulating form as well).

      SELECT tournament.id AS tournament_id, 
           tournament.date_created AS tournament_date_created, 
           tournament.date_modified AS tournament_date_modified, 
           tournament.name AS tournament_name, 
           tournament.player_count AS tournament_player_count, 
           tournament.account_id AS tournament_account_id, 
           tournament.description AS tournament_description, 
           tournament.started AS tournament_started 
           FROM tournament 
           WHERE tournament.id = ?

- User can click the `delete tournament` button to delete the specific tournament (need to also delete from players table).

      DELETE FROM players WHERE tournament_id = ?
      
      DELETE FROM tournament WHERE tournament.id = ?

- User can fill out a form with name, maximum player count and optional description prepopulated with old information to edit the specific tournament.

      UPDATE tournament 
      SET date_modified=CURRENT_TIMESTAMP, name=?, player_count=?, description=? 
      WHERE tournament.id = ?

### When user is logged in and in a specific tournament that has started

- User can see the whole bracket with all the matches.

      SELECT match.id AS match_id_1, 
            match.date_created AS match_date_created, 
            match.date_modified AS match_date_modified, 
            match.tournament_id AS match_tournament_id, 
            match.match_id AS match_match_id, 
            match.round_number AS match_round_number, 
            match.player1_id AS match_player1_id, 
            match.player2_id AS match_player2_id, 
            match.player1_name AS match_player1_name, 
            match.player2_name AS match_player2_name, 
            match.player1_score AS match_player1_score, 
            match.player2_score AS match_player2_score,
            FROM match 
            WHERE match.tournament_id = ? ORDER BY match.match_id

- If user is participating then the user can hover mouse inbetween their matches to reveal the `report result` button and click it trigger report result form (user interface feature and do not have SQL statements).
- If user is the creator of the tournament, then the user has access to all the `report result` buttons in the bracket (user interface feature and do not have SQL statements).

### When the user is logged in, still in a specific tournament that has started and triggered the report result form

- User can submit scores for matches that they are participating in and choose a winner

      (Depending on from which side the bracket the selected winner comes from, we update the following match with current match           
      winners account_id)

      UPDATE match SET player1_id = ? WHERE match_id = ? AND tournament_id = ?
      or
      UPDATE match SET player2_id = ? WHERE match_id = ? AND tournament_id = ?
 
      (We have to also update the scores of the current match)

      UPDATE "match" SET date_modified=CURRENT_TIMESTAMP, player1_score=?, player2_score=?          
            WHERE "match".id = ?

- If user is the creator of the tournament, then the user can also delete matches starting from the leaflets (the select max round number is used to check if we are deleting a leaflet or not). 

      SELECT MAX(round_number) FROM match WHERE tournament_id = ?
      
      DELETE FROM "match" WHERE "match".id = ?

