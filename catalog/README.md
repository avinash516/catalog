## Item-Catalog Shoe Carnival 
By Chekuri Avinash

## About the My Project :
   
This is web application to  build with python framework flask.This application gives   information about Top Company Shoes in  Market and Price of the brands and types and Available Colors to users.



## Requirements
 
- python
 3 or python 2.7
- Flask Framework

- Oauth2client
   
- SQLAlchemy
 
 - Requests
  
- Front End Technologies (HTML ,CSS , JS)
## ``Files in My projec``
 
- shoes.db ------> is the sqllite3 database file.
  
- sample_database.py -----> Sample Data Stored in database.
 
- client_secrets.json -----> File contains oauth2 information.
  
- sampledatabase.py -----> is the database setup file which create tables in the sqllite3 database using sqlalchemy
  
- Static Folder ---->This folder contains the static files such as
  css,javascript,images etc.
  
- Templates Folder ----> This folder contains the all html files only which is used to  rendering data purpose


## `Oauth`
  This application authenticates users using Google Oauth v2 api and stores user data in database.
  More [about](https://developers.google.com/identity/protocols/OAuth2) Google Oauth

  For this api to work you need to have `client_secrets.json` which can downloaded from
  [Google Api Console](https://console.developers.google.con)
  Then
   
 - Create a new project
   
 - Go to credentials page and update your information
   
 - Download the client_secrets.json file and place it project directory



## How to `RUN` server
  :
-In order to run this server you need to install python(3.7) or lower versions in your machine(linux/windows).

  It  recommended to use vagrant for testing  purpose.This will not effect your machine configurations.
 
-directly download vagrant file from FSND_virtual Machine which is given by udacity instructions or we can download individually from online.
- Here is [documentation](https://www.vagrantup.com/docs/) to install vagrant and [virtual box]      (https://www.virtualbox.org/wiki/Documentation)
  
  These instructions assume you have the Udacity-provided Virtual machine
  
  Clone the Udacity Vagrantfile
  
and   Go to Vagrant directory and either clone this repo or download and place zip here
  
  `vagrant up`
  `vagrant ssh`

 Connecting vagrant after goto to Shared folders,
-goto Project Folder
 The entry point for this project is shoes_project.py
  run this file using
  ```
  $python  shoes_project.py

  ```
  
After this if all goes well access your web application from [http://localhost:5000]
 
## `JSON Endpoint`

  -'/brand/JSON'- Displays the Brands and Models data
  
  - '/brand/<int:brand_id>/JSON'


## Help Content from 
 
--- Udacity  Fullsatck Videos

--- www.w3schools.com
  
--- www.tutorialspoint.com   

--- www.stackoverflow.com

--- www.youtube.com
 
 
