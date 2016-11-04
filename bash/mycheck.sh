#!/bin/bash
# do not include full quotes in ANY argument
# 1 is the host to check on
# 2 is the schema pattern match (e.g. %People%)
# 3 is the value to check for each schema
# 4 is the table to check that value in
# 5 is the where condition of the check

mysql -h $1 information_schema -ss -e "select distinct(SCHEMA_NAME) from information_schema.SCHEMATA where SCHEMA_NAME like '$2';" | while read schema;
do
  echo $(mysql -h $1 $schema -ss -e "select $3 from $4 where $5;")
done

