## Description
This is an ETL application which will create a database and dimension and fact tables 
The tables store data used to analyze date regarding songs and user activity collected from 
a music streaming app. The data is sourced from json files 

## Software required
* Postgres
* Python 3.7

## Instructions
* install and launch Posgress
* install Python
* clone the project
* execute create_tables.py to create database
* execute etl.py to perform ETL process 

## Files/descriptions
* README.md - contains project/app details
* create_tables.py - python code to create database and tables
* etl.py - python code to execute ETL process
* sql_queries.py - SQL statements used by create_tables.py and etl.py

## Database Info
The following tables are created in the Postgres database
* Fact Table
  - songplay_fact - records in log data associated with song plays 

* Dimension Tables
  - user_dim - stores users in the app

  - song_dim - stores song details

  - artist_dim - stores artists info

  - time_dim - records time dimension details

## Creator

* Ed Flemister
    - [https://github.com/eflemist/dmwithpostgres](https://github.com/eflemist/dmwithpostgres)
 
 
