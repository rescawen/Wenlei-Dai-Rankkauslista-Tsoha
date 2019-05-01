# Limitations of the Project and Incomplete Features

## The limitations of the work and application 

Due to the limitations of Jinja2 template engine, the templates file sizes grow very big and it is not easy to separate necessary parts to "components" found in other more comprehensive frameworks. For example when you have a index page and you want to display different things depending on whether a user has logged in or not, we are almost rendering 2 different pages under a if statement. 

Custom made sql statements using text cannot be used for pagination. The official pagination is only supported by the basequery object. 

Match deletion breaks the front end of rendering. The plan was just to get a walking skeleton/vertical integration working first which included the joining of tournaments, generating matches for any amount of players and submitting match results properly. I did not forsee the complications of how difficult it is to just get the most basic version of rendering the bracket. 

After generating all the matches in tour_start I was unable to finish the plan of automatically pushing forward players who have essentially a bypass for their first matches. In other words if a player has a placeholder `Player 2` as their opponent it would automatically detect it, push the player to the next match and delete the placeholder match completely.

## The features that are left out of the work. 

The start time for a tournament is usually a very important feature which is left out due to problems in the front end. The input field for the datetime was not straight forward and did not come natively with HTML5 for example in the firefox browser. 

Leaving the tournament. 

Seeding is completely left out. Seeding should be part of this application to begin with. However usually seeding is done by a combination of "ladder" ranking and "tournament" ranking if it is done properly. It is usually the admins job to manually to search for these and especially put the highest ranked players on opposite side of bracket when there is prizes involved. 

The technical of way of implementing seeding would be to create the matches empty without players in it. In our case the unique player IDs, then depending on the seeding we manually insert the players who highest to opposite sides of bracket and continue this until all the players are inserted. 

## Future development plans

Ideally the perfect way is to have the "Ranking websites/servers" plug their data into the tournament system and then there wouldn't manual labour seeding. There would be recommended seeding and admin can just confirm or slightly tweak it before starting the tournament.

Now that I have been focusing on the backend, the frontend could be a similar level project in scope. When you take into account for other bracket formats such as double elimination and group stages etc. 

## How accurate is the documentation planning to the actual final code

Due to the fact that this application is straight forward from a user perspective, the orginal plans are very much represented in the final work. 
