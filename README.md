# Projet_8_DjangoNutella										Projet_8_DjangoNutella
								Créez GrandPy Bot, le papy-robot
								 OpenClassroom's project number 8
										
     									Django_Python_Heroku 
										 Python 3.8.1                          

# SUM UP: 
Projet_8_DjangoNutella is a school project program providing substitutes for specifical fooditem.
On the home page user can ask for a substitute trought a formular, writting the name of a fooditem.
The program search in its database a subsitute with a nutriscore equal of higher than the fooditem's one.
The result is display in a new window. The user could have more information with clicking on the substitute's name.
An app for account creation is also available. It allowed user to save substitutes and consult them in one's personnal history page.
This programme is also deployed on heroku. 

The fooditems datas are composed of following elements:
-Name.
-Brand.
-Nutriscore.
-Ingredients.
-Allergens.
-Store where the fooditem can be purchased.
-Picture.
-Link to OpenFoodFact page.

For login an email adress and a password are required.

## Settings:
For developpement only the debug mode and the debug toolbar are activated.
For more informations about program's settings consult the file settings.py in folder "project_nutella".

## Librairies:
Python libraries are specified in the file "requirements.txt".

## Running program:
### On the Web:
For running this program on the web connect to https://djangonutella.herokuapp.com. 

### On local:
For running it localy:
    1-Install Postgre SQL and create a database "nutella".
    2-Install the requirements.txt settings.
    3-A secret key is also requiered.
    Define your secret key then create a file '.env' and put it inside under the name "SKEY".
    4-Create tables within your database using the command "python manage.py migrate" in the consol.
    5-Insert datas in nutella database using the command "python manage.py init_db".
    5-Finally run the program with the command "python manage.py runserver".
The home page is being displayed at local port:8000.

# AUTHOR:
T.Salgues.

# LICENCE:
Projet_8_DjangoNutella is a public project with a public licence.
For more information read the file: license

# CONVENTIONS:
## Python code:
    Python code respect the PEP8 convention.
    Each class have its file.
    
    For docstring apply the following field
    """" <Description>
    <Arguments>
        Arg 1: type (default value, description)
        Arg 2: type (default value, description)
        ...
    <Return>
        Return 1: type (default value, description)
        Return 2: type (default value, description)
        ...
    <Example>
    """

## Tests:
    Tests are running with Django module test and Selenium.
    Each module is tested by a specofic test's file and use constants of config.py to control right answer of the program.

    Test coverage has to be higher than 80%.

    When adding new APP or any modification to initial APP's, please put your tests in the "tests" folder of the appropriate APP. 

## Constants:
    Global constants are contained in te config.py file in "food_selector" folder.
    When adding constants, please respect the type "dict" of those module's objects.
    

# CONTRIBUTIONs:
Source code is on https://github.com/Thibault231/P_8_django_nutella.
Use a  CONTRIBUTING.md type file to contribute.

# CREDITS:
Special thanks for Cyril.C, Openclassrooms and OpenFoodFact.
