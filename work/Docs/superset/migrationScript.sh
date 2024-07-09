#!/bin/bash

# Start the Superset and PostgreSQL containers
docker-compose -f docker-compose-non-dev up -d

# Wait for containers to initialize
sleep 1m

# Dump the database from the existing PostgreSQL container
docker exec -it superset_db pg_dump -U superset -d superset -F c -f mydatabase_dump.custom

# Copy the dump file from the Superset app container to the host
docker cp superset_app:/mydatabase_dump.custom ./

# # Stop the Superset and PostgreSQL containers
# docker-compose -f docker-compose-non-dev down

# # Wait for containers to stop
# sleep 1m

# # Start the updated version of Superset and PostgreSQL
# docker-compose -f docker-compose-non-dev4.0.0 up -d

# # Wait for containers to initialize
# sleep 5m

# # Copy the dump file into the new PostgreSQL container
# docker cp ./mydatabase_dump.custom superset_db:/

# # Access PostgreSQL container
# # Drop existing schema

# docker exec -it superset_db psql -U superset -c "DROP SCHEMA IF EXISTS public CASCADE;"

# # If the dump is not inside the container, copy it
# docker cp ./mydatabase_dump.custom superset_db:/

# # Restore the dump from another tab inside the container
# docker exec -it superset_db pg_restore -U superset -d superset -F c mydatabase_dump.custom

