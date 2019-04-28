# Installation Guide 

## Installation

Installation may vary depending on platform. For example on windows it is not necessary to activate a virtual environment. 

### Local Installation

Clone this repository with the command or other corresponding ways:

`git clone https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha.git`

Move to the root directory of the cloned folder:

`cd Wenlei-Dai-Rankkauslista-Tsoha`

Create the virtual environment:

`python3 -m venv venv`

Activate the virtual enviroment:

`source venv/bin/activate`

Finally install the dependencies in the requirements text file:

`pip install -r requirements.txt`

### Heroku Installation

For this you will need to have both a heroku account and the heroku command line installed.

After completing the local installation in part above, you are ready to proceed to getting things running on heroku. 

Note: make sure the file [Procfile](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/Procfile) is located in the root of the project. The `run:app` "run" corresponds to the file title [run.py](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/run.py) file. If you were to change the title of run.py you need to change it correspondingly in the Procfile and vice versa. 

Start by creating a new place for Heroku:

`heroku create NAME-OF-YOUR-APPLICATION-HERE`

Add the information about Heroku to your local git repository:

`git remote add heroku https://git.heroku.com/NAME-OF-YOUR-APPLICATION-HERE.git`

After this we push our latest code to heroku:

`git add .`
`git commit -m "COMMIT-MESSAGE"`
`git push heroku master`

To set Heroku to use PostgreSQL which is a relational database management system 

`heroku config:set HEROKU=1`
`heroku addons:add heroku-postgresql:hobby-dev`

## Program Execution

Note: the database is situated under [folder database](https://github.com/rescawen/Wenlei-Dai-Rankkauslista-Tsoha/blob/master/application/__init__.py#L11), if the folder does not exist manually create it yourself.

After local installation: 

If you have linux based operating system you must always activate the virtual environment and then run:

`python run.py`
