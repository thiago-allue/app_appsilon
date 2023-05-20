# Use the PostgreSQL base image
FROM postgres:latest

# Set the environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=appsilon_db

# Copy the SQL scripts to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/