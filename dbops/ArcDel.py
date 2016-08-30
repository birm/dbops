"""Delete or archive old records.

This module allows for command line or programtic archival or deletion of
records with a datetime field..
-Ryan Birmingham
"""

from sqlalchemy import create_engine, inspect
from contextlib import contextmanager


class ArcDel(object):
    """An object to keep track of deletion or archival.

    Args:
        field: The datetime field to check against
        oldtime: The date where, before which, action should be taken.
        database: The database to connect to on the connection
        table: The table to act on
        dbtype: The database server type. (e.g: 'my', 'pg', 'lt', 'ms')
            see dbmap for supported types and abbreviations.
        host: A connection string, e.g. mysql://localhost
        limit: Number of records to do per batch, max
        permissions: A dict, list, file, or file path containing username
            and password.
    """

    dbmap = {'my': 'mysql', 'pg': 'postgresql', 'or': 'oracle',
             'ms': 'mssql', 'lt': 'sqlite', 'rs': 'redshift'}

    def __init__(self, field="CreatedAt", oldtime="1970-01-01",
                 database="dual", dbtype="my", host="localhost",
                 limit=10, permissions=None):
        """Intalize object for connection and tracking."""
        raise NotImplementedError("ArcDel under construction")
        self.dbtype = self.dbmap[dbtype]
        # establish that we are not connected
        self.engine = False
        # other variable assignment
        self.limit = limit
        self.host = host
        self.database = database
        self.table = table
        self.field = field
        self.oldtime = oldtime
        # let permissions None work
        if permissions is None:
            self.permissions = None
        else:
            if type(permissions) is dict:
                self.permissions = permissions
            elif type(permissions) is list:
                # convert to dict
                temp_per = {}
                try:
                    temp_per['username'] = permissions[1]
                    temp_per['password'] = permissions[2]
                except IndexError:
                    raise TypeError("permissions missing information")
                self.permissions = temp_per
            else:
                if type(permissions) is not file:
                    try:
                        permissions = open(permissions)
                    except IOError:
                        raise IOError('permissions interpreted as file path,'
                                      'not found')
                    except TypeError:
                        raise TypeError('permissions type not understood')
                permissions = permissions.read().splitlines()
                temp_per = {}
                try:
                    un = [z for z in permissions if z.startswith('user')]
                    pw = [z for z in permissions if z.startswith('password')]
                    temp_per['username'] = un[0].replace("user=", "")
                    temp_per['password'] = pw[0].replace("password=", "")
                except IndexError:
                    raise TypeError("permissions missing information")
                self.permissions = temp_per

    def __repr__(self):
        """Return a string for python."""
        return "ArcDel object acting on " + self.database + ":" + self.table

    def __str__(self):
        """Return a string for command line invoke."""
        a = "ArcDel object acting on " + self.database + ":" + self.table
        return a + " for " + self.field + " beyond " + self.oldtime

    def start(self):
        """Start engine for the specified DB."""
        if self.permissions is not None:
            self.engine = create_engine(self.dbtype + '://' +
                                        self.permissions['username'] + ":" +
                                        self.permissions['password'] + "@" +
                                        self.host)
        else:
            self.engine = create_engine(self.dbtype + '://' +
                                        self.host)
        return self.engine

    @contextmanager
    def connection(self):
        """Manage connection to DB."""
        try:
            if not engine:
                engine = self.start()
            dbcon = engine.connect()
        except BaseException:
            dbcon = False
            errstr = "Error connecting to DB."
            raise RuntimeError(errstr)
        try:
            yield dbcon
        finally:
            dbcon.disconnect()

    def delete(self):
        """Delete records from db where date contition met."""
        with self.connection() as con:
            pass
            # find count of match criteria:
                # delete (n) matches
                # print next match to screen
                # update count

    def archive(self):
        """Archive records from db where date contition met."""
        with self.connection() as con:
            pass
            # find count of match criteria
                # write (n) matches to file
                # print next match to screen
                # update count

if __name__ == "__main__":
    raise NotImplementedError("ArcDel under construction")
