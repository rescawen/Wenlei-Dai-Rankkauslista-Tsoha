# Tournament Bracket List Database Application

[2019 kevään neljännen periodin tietokantasovellus harjoitustyö](https://materiaalit.github.io/tsoha-19/)

Programming languages: Python 3, SQL, HTML, CSS

## Documentation

#### [Heroku Link](https://wenlei-dai-rankkauslista-tsoha.herokuapp.com/)
#### [Userstory](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/userstory.md)
#### [Database Description](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/databasedescription.md), [Database Diagram](https://raw.githubusercontent.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/master/documentation/pictures/tsohatietokantakaaviofinal.jpg)
#### [User Guide](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/userguide.md)
#### [Incomplete Features](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/incompletefeatures.md)

## Topic Description

The main page will show a list of all tournaments (visible even without log in). User can create and log in with an account. Once logged in, user can both create and join these tournaments. Tournaments are in single elimination format and have seedings based on the order of players who have joined it.

The inspiration is a very simple version of [Challonge](https://challonge.com/).

## Installation 
[Complete installation guide](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/documentation/installationguide.md)

Clone this repository and run:

`pip install -r requirements.txt`

## Program Execution

Note: the database is situated under [folder database](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/__init__.py#L11), if the folder does not exist manually create it yourself.

After cloning the repository and installing the dependencies: 

`python run.py`
