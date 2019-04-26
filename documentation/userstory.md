Jokaista käyttötapausta vastaa yksi tietokantakysely. Jos et ole vielä tehnyt, lisää dokumentaatiossasi käyttötapauksiin niihin liittyvät kyselyt.Jos jokin käyttötapaus jää toteuttamatta, merkitse siitä tieto dokumentaatioosi.

# User Story

### When user lands on front/index page unregistered

- User can see a list of all tournaments. For each tournament there is its name and player count displayed. <br/>
  `SELECT * FROM tournament`
- User can log in.
- User can click `Register as new user` in the navigation bar to go to new account registration page.

### When user is in account registration page

- User can fill out a form with name, username and password to register.

### When user is logged in and is in any page

- User can click `Tournament bracket application` in the navigation bar to return index page.
- User can click `Create new tournament` in the navigation bar to go to new tournament creation page.

### When user is logged into index page

- User sees a list of all tournaments. <br/>
  `SELECT * FROM tournament`
- User sees a list of all tournaments it has signed up for. <br/>
- User sees a list of all tournaments it has created and administrates. <br/>
- User can log out
- User can click a tournament name to take them into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged in and in tournament creation page

- User can fill out a form with name, maximum player count and optional description to create a new tournament.

### When user is logged in and in specific tournament that has not started

- User can click the `Join tournament` button to join the specific tournament.
- If user is the creator of the tournament, then the user can choose to start the tournament regardless of the amount of players.

### When user is logged in and in a specific tournament that has started

- User can see the whole bracket.
- If user is participating then the user can hover mouse inbetween their matches and click the `report result` button.
- If user is the creator of the tournament, then the user has access to all the `report result` buttons in the bracket.

### When the user is logged in, still in a specific tournament that has started and triggered the report result form

- User can submit scores for the specific match and choose a winner.
