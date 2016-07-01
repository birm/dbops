dbops
=====
A collection of tools for managing database servers.

Tools:
  **WhereLives**: quickly determine which host a database is on,
    or which databases are on a host.
      Command line:
        ''python -m dbops.WhereLives (search key) (hostlist file)
         (permissions file) (server type) (reverse mode)''
  **DiskCheck**: get a report on which hosts are low on disk space
    Command line:
      ''python -m dbops.DiskCheck (warn threshold, gb) (hostlist file)''

More Tools coming.

Versions of form:
{tool version}.{number of tools}.{small updates}
