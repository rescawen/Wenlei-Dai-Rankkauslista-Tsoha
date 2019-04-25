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

