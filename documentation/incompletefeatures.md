# Limitations of the Project and Incomplete Features

## The limitations of the work and application 

Due to the limitations of Jinja2 template engine, the templates file sizes grow very big and it is not easy to separate necessary parts to "components" found in other more comprehensive frameworks. For example when you have a index page and you want to display different things depending on whether a user has logged in or not, we are almost rendering 2 different pages under a if statement. 

Custom made sql statements using text cannot be used for pagination. The official pagination is only supported by the [basequery object](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.BaseQuery). The pagination implementions for all the tournaments have 3 separate pages. In reality an ideal way to make it is just one all tournaments page, where you can toggle some buttons or tags to choose what category of tournaments you want to browse whether its joined, owned, all or something even more specific.

After generating all the matches in tour_start I was unable to finish the plan of automatically pushing forward players who have essentially a bypass for their first matches. In other words if a player has a placeholder `Player 2` as their opponent it would automatically detect it, push the player to the next match and delete the placeholder match completely.

Match deletion simply breaks the front end of rendering. The plan was just to get a walking skeleton/vertical integration working first which included the joining of tournaments, generating matches for any amount of players and submitting match results properly. 

I did not forsee the complications of how difficult it is to get the most basic version of rendering the bracket working. For example I had to completely add the round_number attrimute to my match object, because the css essentially renders each [round as a separate unordered list](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/templates/tournament/tournament.html#L25). However I must also credit the agile strategy for actually getting something of this quality done for this timeframe. If I would have focused on cleaning up bugs immediately after finishing small feature I might not have ended up with the result of showing a functioning bracket generation and rendition. 

The winner_id column/attribute of the match table which can be seen in the [database diagram](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/pictures/tsohatietokantakaaviofinal.jpg) before the final submission version. It was left out because it served no purpose for the current version of the project. One of the reason why it would be useful goes back to bracket rendering. For example can use it to highlight the winner of a match.

## The features that are left out of the work. 

The start time for a tournament is usually a very important feature which is left out due to problems in the front end. The input field for the datetime was not straight forward and did not come natively with HTML5 for example in the firefox browser. 

Leaving the tournament had issues with conditionally rendering the tournament page. Due to the fact that tournament page was already conditionally rendered with prior/post starting adding another condition of before joining and after joining was difficult. 

Seeding is completely left out without trying. However usually seeding is done by a combination of "ladder" ranking and "tournament" ranking if it is done properly. It is usually the admins job to manually to search for these and especially put the highest ranked players on opposite side of bracket when there is prizes involved. 

The technical of way of implementing seeding would be to create the matches empty without players in it. In our case the unique player IDs, then depending on the seeding we manually insert the players who highest to opposite sides of bracket and continue this until all the players are inserted. 

User customization was completely left out. It is cool to have country flag, team name, and icon present in the rendering of the bracket to create a better storyline for the tournament. However in the [database normalization](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/databasedescription.md) explanation I have prepared my app for a username change. This includes the tournaments the player has played in the past and after changing name it would be easy to identify your nametag in tournaments played a long time ago. Maybe even having 2 different name fields would actually be ideal. The name you originally played with would always be displayed for third party, but from a personal point of view you would always see your own latest username. 

## Future development plans

Ideally the perfect way is to have the "Ranking websites/servers" plug their data into the tournament system and then there wouldn't manual labour seeding. There would be recommended seeding and admin can just confirm or slightly tweak it before starting the tournament.

Now that I have been focusing on the backend, the frontend could be a similar level project in scope. When you take into account for other bracket formats such as double elimination and group stages etc. 

## How accurate is the documentation planning to the actual final code

Due to the fact that this application is straight forward from a user perspective, the orginal plans are very much represented in the final work. 
