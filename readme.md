dbops
=====
A collection of tools for managing database servers.

# Python Tools: #

## WhereLives ##
  quickly determine which host a database is on,
    or which databases are on a host.
      Command line:
        ''python -m dbops.WhereLives (search key) (hostlist file)
         (permissions file) (server type) (reverse mode)''
         
         
## DiskCheck ## 
  get a report on which hosts are low on disk space
    Use full mode to get more detailed information about errors and successes, including md raid
    Command line:
      ''python -m dbops.DiskCheck (warn threshold, gb) (hostlist file) (username) (full mode)''

Bash Tools/Interfaces:

## wl.sh ##
an interface for WhereLives, simplified further.
  
## daud.sh ##
a wrapper for common audit procedures using pt-toolkit.

More Tools coming.
