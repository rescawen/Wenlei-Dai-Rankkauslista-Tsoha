Jokaista käyttötapausta vastaa yksi tietokantakysely. Jos et ole vielä tehnyt, lisää dokumentaatiossasi käyttötapauksiin niihin liittyvät kyselyt.Jos jokin käyttötapaus jää toteuttamatta, merkitse siitä tieto dokumentaatioosi.

# User Story

### When user lands on front/index page unregistered/not logged in

- User can see a partial list of all tournaments. For each tournament there is its name and player count displayed. <br/>
  `SELECT * FROM tournament`
- User can log in.
- User can click `Register as new user` in the navigation bar to go to new account registration page.

### When user is in account registration page

- User can fill out a form with name, username and password to register.

### When user is logged in and is in any page

- User can click `Tournament bracket application` in the navigation bar to return index page.
- User can click `All tournaments` in the navigation bar to go to all tournaments page.
- User can click `Joined tournaments` in the navigation bar to go to joined tournaments page.
- User can click `Owned tournaments` in the navigation bar to go to owned tournaments page.
- User can click `Create new tournament` in the navigation bar to go to new tournament creation page.
- User can log out

### When user is logged into index page

- User sees a partial list of all tournaments. <br/>
  `SELECT * FROM tournament`
- User sees a list of all tournaments it has signed up for. <br/>
- User sees a list of all tournaments it has created and administrates. <br/>
- User can click a tournament name to take them into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged and in all tournaments page

- User sees a partial list of all tournaments. <br/>
  `SELECT * FROM tournament`
- User can continue to browse the rest of all tournaments through pagination.
- User can click a tournament name to take them into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged and in joined tournaments page

- User sees a partial list of all tournaments it has signed up for <br/>
  `SELECT * FROM tournament`
- User can continue to browse the rest of joined tournaments through pagination.
- User can click a tournament name to take them into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged and in owned tournaments page

- User sees a partial list of all tournaments it has created and administrates. <br/>
  `SELECT * FROM tournament`
- User can continue to browse the rest of all tournaments through pagination.
- User can click a tournament name to take them into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged in and in tournament creation page

- User can fill out a form with name, maximum player count and optional description to create a new tournament.

### When user is logged in and in a specific tournament that has not started

- User can click the `Join tournament` button to join the specific tournament.
- If user is the creator of the tournament, then the user can choose to start the tournament regardless of it not reaching maximum player count with a minimum of one player.
- If user is the creator of the tournament, then user can click `edit tournament` button to go to tournament edit page.

### When user is logged in and in tournament editing page as creator of the tournament

- User can click the `delete tournament` button to delete the specific tournament.
- User can fill out a form with name, maximum player count and optional description to edit the specific tournament.

### When user is logged in and in a specific tournament that has started

- User can see the whole bracket.
- If user is participating then the user can hover mouse inbetween their matches to reveal the `report result` button and click it trigger report result form.
- If user is the creator of the tournament, then the user has access to all the `report result` buttons in the bracket.

### When the user is logged in, still in a specific tournament that has started and triggered the report result form

- User can submit scores for matches that they are participating in and choose a winner.
- If user is the creator of the tournament, then the user can also delete matches starting from the leaflets. 
