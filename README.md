# FITSPOGRAM

## About the app

INSPO FOR FITSPO

Fitspogram aims to:

-   allow fitness lovers to share their workout routines
-   allow users who want to start their fitness journey to have inspiration/motivation
-   allow users to access a variety of workouts by different users to try

-   [App](https://cjt-fitspo.herokuapp.com/)

## Installation

Run these commands:

-   `git clone git@github.com:cynthiajteo/fitspo.git`
-   `pipenv shell`
-   `pipenv install django psycopg2-binary`
-   `pipenv run python manage.py makemigrations`
-   `pipenv run python manage.py migrate`
-   `pipenv run python manage.py runserver`

Create .env file and include your own:

-   SECRET_KEY
-   DATABASE_NAME
-   DATABASE_USER
-   PORT
-   CLOUD_NAME (cloudinary)
-   API_KEY (cloudinary)
-   API_SECRET (cloudinary)

## Technologies

-   Django
-   Python
-   PostgreSQL (Database)
-   Psycopg2-binary (PostgreSQL database adapter)
-   Python Dotenv
-   Cloudinary (Cloud storage)
-   Bootstrap 5

## Project Management & Wireframe

-   [GitHub Project](https://github.com/cynthiajteo/fitspo/projects/1)
-   [Wireframe](https://docs.google.com/presentation/d/184MyZmmj8U7LkJyCWNvx2io9vcyR166VJw5bc8eDKjA/edit#slide=id.gdec580192f_0_23)

## Future Developments

-   edit/delete comments
-   include profile pic
-   allow user to follow other users
-   display following and followers
