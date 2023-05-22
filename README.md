# Appsilon Movie Database

This is a web application that provides movie data from a PostgreSQL database. It consists of a front-end and a back-end component. The front-end is built with React, and the back-end is developed using Flask.

## Pre-requisites
### Docker and Docker-Compose
To run the application, you need to have Docker and Docker-Compose installed on your machine.

### Ports
Ensure that the following ports are free on your machine before running the application: 5000, 3000 and 5432.

## Getting Started

1. Clone the repository:

```shell
git clone https://github.com/thiago-allue/app_appsilon
cd app_appsilon
```

2. Build and run the Docker containers:
```shell
sudo docker-compose up --build
```

Access the application:
Once the containers are up and running, you can access the application in your browser at **http://localhost:3000**.

## Application Structure
The repository is organized into the following directories:

- **frontend_appsilon**: Contains the front-end React application.
- **backend_appsilon**: Contains the back-end Flask application.
- **database**: Contains the Dockerfile and initialization script for the PostgreSQL database.

## Front-End
The front-end is built using React and is responsible for displaying the movie data retrieved from the back-end. It provides a user interface to interact with the application.

The source code for the front-end is located in the **frontend_appsilon** directory.

## Back-End
The back-end is developed using Flask, a Python web framework. It handles API requests from the front-end and communicates with the PostgreSQL database to retrieve and store movie data.

The source code for the back-end is located in the **backend_appsilon** directory.

## API Endpoints
The back-end provides the following API endpoints:

- **/retrieve**: Retrieves movie data from Wikidata and creates a **data.json** file.
- **/ingest**: Ingests data from the **data.json** file into the PostgreSQL database.
- **/load_imdbs**: Retrieves IMDb data from the database and returns it as JSON.
- **/load_movies**: Retrieves movie data from the database and returns it as JSON.
- **/delete**: Deletes all data from the PostgreSQL database.
 
## Configuration
The back-end configuration is stored in the **backend_appsilon/config.py** file. It contains the database connection URL and other configuration variables.

## Database
The application uses a PostgreSQL database to store movie data. The database container is defined in the **database/Dockerfile**, and the initialization script is located at **database/init.sql**. The database is automatically initialized when the container is started.
