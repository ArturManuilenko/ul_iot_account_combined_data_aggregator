#!/bin/bash

db="archive"
path=$(realpath backup)

select date in $(ls $path)
do
  docker exec -it postgres psql -U admin device_db -c "CREATE TABLE IF NOT EXISTS audit.$db (LIKE audit.logged_actions);"
  docker exec -it postgres sed -i "s/INTO audit.logged_actions/INTO audit."$db"/g" /mnt/$date
  docker exec -it postgres psql -U admin device_db -c "SELECT COUNT(*) FROM audit.$db;"
  docker exec -it postgres psql -U admin device_db -a audit.archive -f /mnt/$date
  break
done
