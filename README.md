# FITSPOGRAM

## Introduction - Inspo for Fitspo

Fitspogram aims to:

-   allow fitness lovers to share their workout routines
-   allow users who want to start their fitness journey to have inspiration/motivation
-   allow users to access a variety of workouts by different users to try

## App Links

-   [App]()
-   [Project Management](https://github.com/cynthiajteo/fitspo/projects/1)

## Table of Contents

-   [Installation](#Installation)
-   [Technologies](#Technologies)
-   [User Story and Wireframe](#User-Story-and-Wireframe)
-   [Main Features](#Main-Features)
-   [Future Developments](#Future-Developments)

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

## User Story and Wireframe

As a User, I want to:

-   register/sign up/login/logout
-   create own workout with a photo
-   view own workout
-   edit/delete own workout
-   view other users' workouts
-   comment on workouts
-   like workouts for future reference
-   search particular user

[Link to Wireframe](https://docs.google.com/presentation/d/184MyZmmj8U7LkJyCWNvx2io9vcyR166VJw5bc8eDKjA/edit#slide=id.gdec580192f_0_23)

## Main Features

-   create/view/edit/delete workout with photo
-   comment on workout post
-   search particular user
-   auto logout after 1 day

## Future Developments

-   edit own comments
-   include profile pic
-   allow user to follow other users
-   display following and followers
