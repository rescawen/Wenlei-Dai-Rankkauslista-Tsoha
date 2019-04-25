Vaikka SQLalchemy tekee suurimman osan kyselyistä puolestasi, pitää sinunkin tietää ja ymmärtää, mitä kyselyitä todellisuudessa tietokannasta kysytään. Jokaista käyttötapausta vastaa yksi tietokantakysely. Jos et ole vielä tehnyt, lisää dokumentaatiossasi käyttötapauksiin niihin liittyvät kyselyt.Jos jokin käyttötapaus jää toteuttamatta, merkitse siitä tieto dokumentaatioosi.

# User Story

### When user lands on front page

- User can see a list of all tournaments <br/>
  `SELECT * FROM tournament`
- User can click a link that takes you into a specific tournament page and only view it
- User can log in
- User can create a new account

### When user is logged in

- User still sees a list of all tournaments <br/>
  `SELECT * FROM tournament`
- User can log out
- User can create a tournament
- User can click a link that takes you into a specific tournament page <br/>
  `SELECT * FROM tournament WHERE id='tournament.id'`

### When user is logged in and viewing specific tournament

- User can choose to join the specific tournament
- User can be the creator of the tournament and manipulate it by starting it and advancing matches

### When user is signed up for tournament

- User can see the whole bracket
- User can see their current match including their opponent
