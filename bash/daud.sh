#!/bin/bash
# Usage: ./daud hosts like
like_host=$2
for host in $(cat $1); do
  echo "~~~ ### " $host " ### ~~~"
  echo "1 #### Configuration Differences #### 1"
  pt-config-diff h=$like_host h=$host
  echo "2 #### Variable Advising #### 2"
  pt-variable-advisor $host
  echo "3 #### Duplicate Keys #### 3"
  pt-duplicate-key-checker --host $host
done
