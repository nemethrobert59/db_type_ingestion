@echo off
SET PGUSER=postgres
SET PGPASSWORD=mypassword
SET PGHOST=localhost
SET PGPORT=5432

echo Creating the database...
psql -c "CREATE DATABASE your_database_name;"

echo Database created successfully.