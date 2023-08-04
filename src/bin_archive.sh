#!/bin/bash

name="$(date +"%d-%m-%Y")"
docker exec -it postgres pg_dump -U admin --column-inserts --data-only --table=audit.logged_actions device_db -f /mnt/${name}.dump &&
docker exec -it postgres psql -U admin device_db -c "DELETE FROM audit.logged_actions;"
